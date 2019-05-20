package com.idk.bs.web.accounts;

import static com.idk.bs.utils.GlobalUtils.ensureTwoDigitNumber;
import static com.idk.bs.utils.GlobalUtils.sendPdfResponse;
import static com.idk.bs.utils.GlobalUtils.stringIsEmpty;
import static com.idk.bs.utils.GlobalUtils.subListFromPaginator;
import static java.util.Calendar.DAY_OF_MONTH;
import static java.util.Calendar.MONTH;
import static java.util.Calendar.YEAR;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;

import org.apache.commons.collections4.Closure;
import org.apache.commons.collections4.IterableUtils;
import org.apache.commons.lang3.StringUtils;
import org.apache.commons.lang3.math.NumberUtils;
import org.dozer.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

import com.bs.cards.service.models.CardModel;
import com.everis.bs.model.AbstractMovementWrapper;
import com.everis.bs.model.AbstractPeriodMovementModel;
import com.everis.bs.model.GenericGroupedMovementResponse;
import com.everis.bs.model.accounts.InterveningQueryRequest;
import com.everis.bs.model.accounts.InterveningQueryResponse;
import com.everis.bs.model.accounts.enroll.AccountsListEnrollRequest;
import com.everis.bs.model.accounts.enroll.AccountsListEnrollResponse;
import com.everis.bs.model.accounts.movements.AccountMovementWrapper;
import com.everis.bs.model.accounts.movements.GroupedMovementRequest;
import com.everis.bs.model.accounts.position.AccountsPositionRequest;
import com.everis.bs.model.accounts.position.AccountsPositionResponse;
import com.everis.bs.model.errors.OperationGroup;
import com.everis.bs.utils.ParsingHelper;
import com.idk.bs.app.exception.BadRequestException;
import com.idk.bs.app.exception.InternalServerErrorException;
import com.idk.bs.app.exception.NotFoundException;
import com.idk.bs.app.exception.SoapFaultException;
import com.idk.bs.app.versioning.ApiVersion;
import com.idk.bs.model.AccountModel;
import com.idk.bs.model.BaseModel;
import com.idk.bs.model.BooleanResponseModel;
import com.idk.bs.model.DocumentModel;
import com.idk.bs.model.PaginatorModel;
import com.idk.bs.model.accounts.AccountBalancesModel;
import com.idk.bs.model.accounts.AccountMovementModel;
import com.idk.bs.model.accounts.AccountMovementsListModel;
import com.idk.bs.model.accounts.AccountPayersModel;
import com.idk.bs.model.accounts.AccountsListModelV1;
import com.idk.bs.model.cards.CardMovementsDebitSplitModel;
import com.idk.bs.service.accounts.AccountBalanceServiceImpl;
import com.idk.bs.service.accounts.AccountMovementsDocumentServiceImpl;
import com.idk.bs.service.accounts.AccountMovementsReturnBillServiceImpl;
import com.idk.bs.service.accounts.AccountMovementsReturnBillValidationServiceImpl;
import com.idk.bs.service.accounts.AccountMovementsServiceImpl;
import com.idk.bs.service.accounts.AccountPayersServiceImpl;
import com.idk.bs.service.accounts.AccountsEnrollServiceImpl;
import com.idk.bs.service.accounts.AccountsServiceImpl;
import com.idk.bs.service.alias.AliasServiceImpl;
import com.idk.bs.service.cards.CardMovementsDebitSplitServiceImpl;
import com.idk.bs.utils.GlobalUtils;
import com.idk.bs.web.BaseController;
import com.idk.bs.web.card.CardMovementsDebitSplitForm;

/**
 *
 * @author marcserra
 */
@Controller
@OperationGroup(name ="accounts")
public class AccountsController extends BaseController {

    /**
     * Card movement simple ofuscation pattern.
     */
    private static final String CARD_MOVEMENT_SIMPLE_OBFUSCATION_REPLACEMENT = "..";

    /**
     * Card movement original ofuscation pattern.
     */
    private static final String CARD_MOVEMENT_ORIGINAL_OBFUSCATION_PATTERN = "X{8}";

    /**
     * Card movement String pattern.
     */
    private static final String CARD_MOVEMENT_STRING_PATTERN = "\\p{Blank}?\\p{Digit}{4}" + CARD_MOVEMENT_ORIGINAL_OBFUSCATION_PATTERN + "\\p{Digit}{4}";

    /**
     * Card movement pattern.
     */
    private static final Pattern CARD_MOVEMENT_PATTERN = Pattern.compile(CARD_MOVEMENT_STRING_PATTERN);
    
    /**
     * Bizum.
     */
    private static final String BIZUM = "BIZUM";
    
    /**
     * Utility helper for parsers.
     */
    @Autowired
    private ParsingHelper parsingHelper;
    
    /**
     * Dozer mapper.
     */
    @Autowired
    private Mapper accountMovementsMapper;
    
    private AccountsServiceImpl accountsService;
    private AccountMovementsServiceImpl accountMovementsService;
    private AccountMovementsDocumentServiceImpl accountMovementsDocumentService;
    private AccountMovementsReturnBillValidationServiceImpl accountMovementsReturnBillValidationService;
    private AccountMovementsReturnBillServiceImpl accountMovementsReturnBillService;
    private AccountPayersServiceImpl accountPayersService;
    private AccountBalanceServiceImpl accountBalanceService;
    private AliasServiceImpl aliasService;
    private CardMovementsDebitSplitServiceImpl cardMovementsDebitSplitService;
    @Autowired
    private AccountsEnrollServiceImpl accountsEnrollService;
    
    /**
     * Gives accounts list
     *
     * @param accountForm
     * @param result
     * @param request
     * @param response
     * @return AccountsListModel
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws com.idk.bs.app.exception.NotFoundException
     */
    @RequestMapping(value = "/accounts", method = RequestMethod.GET)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    AccountsListModelV1 getAccountsList(@Valid @ModelAttribute AccountsForm accountForm,
            BindingResult result, HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, NotFoundException {

        AccountsListModelV1 responseModel;
        accountForm.setSessionId(session.getSessionId());
        accountForm.setProduct(session.getProduct());

        try {// Everis code
            responseModel = (AccountsListModelV1) accountsService.getAccountsList(accountForm);
            // START Everis code
        } catch (SoapFaultException e) {
            if ((e.getModel().getErrorMessage().contains(NO_ACCOUNTS_ERROR) || e.getModel().getErrorMessage().contains(NO_PRODUCTS_AVAILABLE))
                    && Boolean.parseBoolean(request.getParameter(NO_ERROR_PARAMETER_NAME))) {
                responseModel = new AccountsListModelV1();
            } else {
                throw e;
            }
        }
		// END Everis code

        //filter shareholders accounts
        ArrayList<AccountModel> accounts = new ArrayList<>();
        for (AccountModel account : responseModel.getAccounts()) {
            if (!"DV00130".equalsIgnoreCase(account.getProduct())) {
                accounts.add(account);
            }
        }
        responseModel.setAccounts(accounts);

        PaginatorModel paginator = new PaginatorModel();
        paginator.setTotalItems(responseModel.getAccounts().size());
        if (accountForm.getPage() != null) {
            paginator.setPage(accountForm.getPage());
            if (accountForm.getItemsPerPage() != null) {
                paginator.setItemsPerPage(accountForm.getItemsPerPage());
            }
            if (accountForm.getOrder() != null) {
                paginator.setOrder(accountForm.getOrder());
            }

            responseModel.setAccounts(subListFromPaginator(paginator, responseModel.getAccounts()));
        }
        responseModel.setPaginator(paginator);
        return responseModel;

    }

    /**
     * Generate a global position with accounts.
     * 
     * @param accountForm
     *            Data to request the original account list.
     * @param result
     *            Validation data.
     * @param request
     *            Input HTTP data.
     * @param response
     *            Output HTTP data.
     * @return The account position.
     * @throws Exception
     *             If server fails.
     */
    @RequestMapping(value = "/accounts/position", method = RequestMethod.GET)
    @ApiVersion(minValue = 1750, maxValue = 1859)
    public @ResponseBody AccountsPositionResponse getAccountsPosition(@Valid @ModelAttribute AccountsPositionRequest restRequest,
            BindingResult result, HttpServletRequest request, HttpServletResponse response) throws Exception {
        try {
            return accountsService.getAccountsPosition(getAccountsList(restRequest, result, request, response));
        } catch (Exception e) {
            logger.logException(getClass(), e);
            throw parsingHelper.advancedParse(e);
        }
    }
    
    /**
     * Generate a global position with accounts.
     * 
     * @param accountForm
     *            Data to request the original account list.
     * @param result
     *            Validation data.
     * @param request
     *            Input HTTP data.
     * @param response
     *            Output HTTP data.
     * @return The account position.
     * @throws Exception
     *             If server fails.
     */
    @RequestMapping(value = "/accounts/position", method = RequestMethod.GET)
    @ApiVersion(minValue = 1860)
    public @ResponseBody AccountsPositionResponse getAccountsPositionV1860(@Valid @ModelAttribute AccountsPositionRequest restRequest,
            BindingResult result, HttpServletRequest request, HttpServletResponse response) throws Exception {
        try {
        	AccountsPositionResponse restResponse;
        	restResponse = accountsService.getAccountsPosition(getAccountsList(restRequest, result, request, response));
        	
        	/* Encription */
            for (AccountModel account : restResponse.getAccountGroupList().iterator().next().getAccountModelList()) {
                GlobalUtils.generateHashIban(account);
            }
        	
            return restResponse;
        } catch (Exception e) {
            logger.logException(getClass(), e);
            throw parsingHelper.advancedParse(e);
        }
    }

    /**
     * Gives the movements list of the given account
     *
     * @param accountMovementsForm
     * @param request
     * @param response
     * @return AccountMovementsListModel
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws BadRequestException
     */
    @RequestMapping(value = "/accounts/movements", method = RequestMethod.POST)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    AccountMovementsListModel getAccountMovementsList(@Valid @RequestBody AccountMovementsForm accountMovementsForm,
            HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, BadRequestException {

        accountMovementsForm.setSessionId(session.getSessionId());
        accountMovementsForm.setProduct(session.getProduct());

        // Prepare dates to filter(currently we get the movements from the last 3 month)
        if (stringIsEmpty(accountMovementsForm.getDateFrom()) || stringIsEmpty(accountMovementsForm.getDateTo())) {
            Calendar calFrom = Calendar.getInstance();
            calFrom.add(Calendar.MONTH, -6);
            Calendar calTo = Calendar.getInstance();
            calTo.add(Calendar.YEAR, +50);

            accountMovementsForm.setDateFrom(ensureTwoDigitNumber(String.valueOf(calFrom.get(DAY_OF_MONTH))) + "-" + ensureTwoDigitNumber(String.valueOf(calFrom.get(MONTH) + 1)) + "-" + String.valueOf(calFrom.get(YEAR)));
            accountMovementsForm.setDateTo(ensureTwoDigitNumber(String.valueOf(calTo.get(DAY_OF_MONTH))) + "-" + ensureTwoDigitNumber(String.valueOf(calTo.get(MONTH) + 1)) + "-" + String.valueOf(calTo.get(YEAR)));

        }

        AccountMovementsListModel responseModel = (AccountMovementsListModel) accountMovementsService.getAccountMovements(accountMovementsForm, session.isCompany());

        return responseModel;

    }

    /**
     * Group account movements.
     * 
     * @param groupedMovementRequest
     *            REST request to query account movements.
     * @param request
     *            HTTP entity.
     * @param response
     *            HTTP entity.
     * @return Account movement group.
     * @throws Exception
     *             If an error has been detected.
     */
    @RequestMapping(value = "/accounts/movements/grouped", method = RequestMethod.POST)
    @ApiVersion(minValue = 1750, maxValue = 1859)
    public @ResponseBody GenericGroupedMovementResponse getAccountMovementsListGroup(
        @Valid @RequestBody GroupedMovementRequest groupedMovementRequest, HttpServletRequest request, HttpServletResponse response)
        throws Exception {
        /* Old call */
        AccountMovementsForm oldForm = accountMovementsMapper.map(groupedMovementRequest, AccountMovementsForm.class);
        AccountMovementsListModel oldModel = getAccountMovementsList(oldForm, request, response);
        
        /* Encription */
        GlobalUtils.generateHashIban(oldModel.getAccount());

        /* Service call */
        GenericGroupedMovementResponse restResponse = accountMovementsService.getAccountMovementsListGroup(oldModel);

        /* Response fixing */
        if (restResponse != null) {
            restResponse.setMoreElements(oldModel.isMoreElements());

            /* JV-48645: BSM - Modificar literal movimientos de cuenta */
            fixCardConcept(restResponse);
        }

        return restResponse;

    }
    
    /**
     * Group account movements.
     * 
     * @param groupedMovementRequest
     *            REST request to query account movements.
     * @param request
     *            HTTP entity.
     * @param response
     *            HTTP entity.
     * @return Account movement group.
     * @throws Exception
     *             If an error has been detected.
     */
    @RequestMapping(value = "/accounts/movements/grouped", method = RequestMethod.POST)
    @ApiVersion(minValue = 1860)
    public @ResponseBody GenericGroupedMovementResponse getAccountMovementsListGroupV1860(
        @Valid @RequestBody GroupedMovementRequest groupedMovementRequest, HttpServletRequest request, HttpServletResponse response)
        throws Exception {
        /* Old call */
        AccountMovementsForm oldForm = accountMovementsMapper.map(groupedMovementRequest, AccountMovementsForm.class);
        AccountMovementsListModel oldModel = getAccountMovementsList(oldForm, request, response);
        
        /* Service call */
        GenericGroupedMovementResponse restResponse = accountMovementsService.getAccountMovementsListGroup(oldModel);

        /* Response fixing */
        if (restResponse != null) {
            restResponse.setMoreElements(oldModel.isMoreElements());

            /* JV-48645: BSM - Modificar literal movimientos de cuenta */
            fixCardConcept(restResponse);
        }

        return restResponse;

    }

    /**
     * Relocate the card number in account movement's concept.
     * 
     * @param restResponse
     *            REST response with account movement groups.
     */
    private void fixCardConcept(GenericGroupedMovementResponse restResponse) {
        IterableUtils.forEach(restResponse.getPeriodMovementModelList(), new PeriodMovementModelListClosure());
    }

    /**
     * Explore each movement into a movement group.
     * 
     * @author friosnar
     */
    private class PeriodMovementModelListClosure implements Closure<AbstractPeriodMovementModel> {

        /**
         * {@inheritDoc}
         */
        @Override
        public void execute(AbstractPeriodMovementModel abstractPeriodMovementModel) {
            if ((abstractPeriodMovementModel != null) && (abstractPeriodMovementModel.getGenericMovementWrapperList() != null)) {
                IterableUtils.forEach(abstractPeriodMovementModel.getGenericMovementWrapperList().getMovements(),
                        new AccountMovementWrapperClosure());
            }
        }

    }

    /**
     * Update the movement concept if matchs.
     * 
     * @author friosnar
     * @see CARD_MOVEMENT_STRING_PATTERN
     */
    private class AccountMovementWrapperClosure implements Closure<AbstractMovementWrapper> {

        /**
         * {@inheritDoc}
         */
        @Override
        public void execute(AbstractMovementWrapper abstractMovementWrapper) {
            if ((abstractMovementWrapper != null) && (abstractMovementWrapper instanceof AccountMovementWrapper)) {
                AccountMovementModel accountMovementModel = ((AccountMovementWrapper) abstractMovementWrapper).getAccountMovement();

                if ((accountMovementModel != null) && (accountMovementModel.getConcept() != null)) {
                    Matcher matcher = CARD_MOVEMENT_PATTERN.matcher(accountMovementModel.getConcept());

                    if (matcher.find()) {
                        String cardNumber = matcher.group(NumberUtils.INTEGER_ZERO);

                        if (cardNumber != null) {
                            String newCardNumber = cardNumber.replaceAll(CARD_MOVEMENT_ORIGINAL_OBFUSCATION_PATTERN,
                                    CARD_MOVEMENT_SIMPLE_OBFUSCATION_REPLACEMENT);

                            if (!newCardNumber.startsWith(StringUtils.SPACE)) {
                                newCardNumber = StringUtils.SPACE.concat(newCardNumber);
                            }

                            accountMovementModel
                                    .setConcept(accountMovementModel.getConcept().replaceFirst(cardNumber, StringUtils.EMPTY).concat(newCardNumber));
                        }
                    }
                }
            }
        }

    }

    /**
     * Gives payers list
     *
     * @param accountForm
     * @param request
     * @param response
     * @return
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws BadRequestException
     */
    @RequestMapping(value = "/accounts/payers", method = RequestMethod.POST)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    BaseModel getAccountPayers(@Valid @RequestBody AccountPayersForm accountForm,
            HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, BadRequestException {

        accountForm.setSessionId(session.getSessionId());
        accountForm.setProduct(session.getProduct());

        AccountPayersModel responseModel = (AccountPayersModel) accountPayersService.getAccountPayers(accountForm);

        return responseModel;
    }

    /**
     * Gives an account movement document
     *
     * @param accountMovementsDocumentForm
     * @param result
     * @param request
     * @param response
     * @return
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws UnsupportedEncodingException
     * @throws IOException
     */
    @RequestMapping(value = "/accounts/movements/document", method = RequestMethod.POST)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    BaseModel getAccountMovementsDocumentList(@Valid @RequestBody AccountMovementsDocumentForm accountMovementsDocumentForm,
            BindingResult result, HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, UnsupportedEncodingException, IOException {
        DocumentModel responseModel = null;

        accountMovementsDocumentForm.setSessionId(session.getSessionId());
        accountMovementsDocumentForm.setProduct(session.getProduct());
        responseModel = (DocumentModel) accountMovementsDocumentService.getAccountMovementsDocument(accountMovementsDocumentForm);

        if (stringIsEmpty(accountMovementsDocumentForm.getFormat())) {
            accountMovementsDocumentForm.setFormat("");
        }
        switch (accountMovementsDocumentForm.getFormat()) {
            case "pdf":
                String fileName = responseModel.getName();
                sendPdfResponse(fileName, responseModel.getContent(), request, response);
                return null;
        }
        return responseModel;
    }

    /**
     *
     * @param accountMovementsReturnBillForm
     * @param result
     * @param request
     * @param response
     * @return
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws UnsupportedEncodingException
     * @throws IOException
     */
    @RequestMapping(value = "/accounts/movements/returnbill", method = RequestMethod.POST)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    BaseModel accountMovementsReturnBill(@Valid @RequestBody AccountMovementsReturnBillForm accountMovementsReturnBillForm,
            BindingResult result, HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, UnsupportedEncodingException, IOException {
        BooleanResponseModel responseModel = null;

        accountMovementsReturnBillForm.setSessionId(session.getSessionId());
        accountMovementsReturnBillForm.setProduct(session.getProduct());
        BooleanResponseModel validate = (BooleanResponseModel) accountMovementsReturnBillValidationService.accountMovementsReturnBillValidation(accountMovementsReturnBillForm);
        if (validate.isResult()) {
            responseModel = (BooleanResponseModel) accountMovementsReturnBillService.accountMovementsReturnBill(accountMovementsReturnBillForm);
        }

        return responseModel;

    }

    @ResponseStatus(value = HttpStatus.OK)
    @RequestMapping(value = "/accounts/movements/debitsplit", method = RequestMethod.POST)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    BaseModel putCardMovementsDebitSplitPeriods(@Valid @RequestBody AccountMovementsDebitSplitForm form,
            BindingResult result, HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, UnsupportedEncodingException, IOException {

        CardMovementsDebitSplitModel responseModel;

        CardMovementsDebitSplitForm cardMovementsDebitSplitForm = new CardMovementsDebitSplitForm();
        cardMovementsDebitSplitForm.setSessionId(session.getSessionId());
        cardMovementsDebitSplitForm.setProduct(session.getProduct());
        cardMovementsDebitSplitForm.setTAE(appProperties.getDebitSplitTAE());
        cardMovementsDebitSplitForm.setAccountMovement(form.getAccountMovement());
        cardMovementsDebitSplitForm.setCreditCard(form.getCreditCard());
        cardMovementsDebitSplitForm.setPeriod(form.getPeriod());
        cardMovementsDebitSplitForm.setPhoneNumber(form.getPhoneNumber());
        cardMovementsDebitSplitForm.setIdioma(form.getIdioma());
        cardMovementsDebitSplitForm.setImporteValue(form.getImporteValue());
        cardMovementsDebitSplitForm.setSecondKey(form.getSecondKey());

        //set debit card related
        CardModel debitCard = new CardModel();
        debitCard.setNumber(form.getAccountMovement().getNumPAN());
        cardMovementsDebitSplitForm.setDebitCard(debitCard);

        responseModel = (CardMovementsDebitSplitModel) cardMovementsDebitSplitService.postCardMovementsDebitSplit(cardMovementsDebitSplitForm);

        if (responseModel.isDebitSplitOk()) {
            return responseModel;
        } else {
            throw new InternalServerErrorException();
        }

    }

    /**
     * Gives account balance of given account
     *
     * @param form
     * @param result
     * @param request
     * @param response
     * @return
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws UnsupportedEncodingException
     * @throws IOException
     */
    @RequestMapping(value = "/accounts/balance", method = RequestMethod.POST)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    BaseModel accountBalanceBill(@Valid @RequestBody AccountForm form,
            BindingResult result, HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, UnsupportedEncodingException, IOException {
        AccountBalancesModel responseModel = null;

        form.setSessionId(session.getSessionId());
        form.setProduct(session.getProduct());
        responseModel = (AccountBalancesModel) accountBalanceService.getAccountBalance(form);

        return responseModel;

    }

    /**
     * Sets the account Alias
     *
     * @param form
     * @param result
     * @param request
     * @param response
     * @return
     * @throws InternalServerErrorException
     * @throws SoapFaultException
     * @throws UnsupportedEncodingException
     * @throws IOException
     */
    @ResponseStatus(value = HttpStatus.OK)
    @RequestMapping(value = "/accounts/alias", method = RequestMethod.PUT)
    @ApiVersion(minValue = 1)
    public @ResponseBody
    BaseModel setAlias(@Valid @RequestBody AccountForm form,
            BindingResult result, HttpServletRequest request, HttpServletResponse response)
            throws InternalServerErrorException, SoapFaultException, UnsupportedEncodingException, IOException {

        BooleanResponseModel responseModel;

        form.setSessionId(session.getSessionId());
        form.setProduct(session.getProduct());
        responseModel = (BooleanResponseModel) aliasService.setAccountAlias(form);

        return responseModel;
    }

    /**
     * Query account's interveners.
     * 
     * @param restRequest
     *            REST model with the account.
     * @return REST response with the account's interveners.
     * @throws Exception
     *             If an error has been detected.
     */
    @ResponseStatus(value = HttpStatus.OK)
    @RequestMapping(value = "/accounts/interveners", method = RequestMethod.POST)
    @ApiVersion(minValue = 1750)
    public @ResponseBody InterveningQueryResponse getInterveners(@Valid @RequestBody InterveningQueryRequest restRequest) throws Exception {
        try {
            return accountsService.getInterveners(session, restRequest);
        } catch (Exception e) {
            logger.logException(getClass(), e);
            throw parsingHelper.advancedParse(e);
        }
    }
    
    /**
     * Bizum Account's enroll.
     * 
     * @param restRequest
     *            Empty REST model.
     * @return REST response with the account to Bizum enroll.
     * @throws Exception
     *             If an error has been detected.
     */
    @ResponseStatus(value = HttpStatus.OK)
    @RequestMapping(value = "/accounts/enroll", method = RequestMethod.GET)
    @ApiVersion(minValue = 1850)
    public @ResponseBody AccountsListEnrollResponse getAccountsEnroll(@Valid @ModelAttribute AccountsListEnrollRequest restRequest, HttpServletRequest request,
            HttpServletResponse response) throws Exception {
        try {
        	if (BIZUM.equals(restRequest.getEnrollable())) {
                return accountsEnrollService.getAccountsEnroll(session, restRequest);
            }
        } catch (Exception e) {
            throw e;
        }
		return null;
    }

    @Autowired
    public void setAccountsService(AccountsServiceImpl accountsService) {
        this.accountsService = accountsService;
    }

    @Autowired
    public void setAccountMovementsService(AccountMovementsServiceImpl accountMovementsService) {
        this.accountMovementsService = accountMovementsService;
    }

    @Autowired
    public void setAccountMovementsDocumentService(AccountMovementsDocumentServiceImpl accountMovementsDocumentService) {
        this.accountMovementsDocumentService = accountMovementsDocumentService;
    }

    @Autowired
    public void setAccountMovementsReturnBillValidationService(AccountMovementsReturnBillValidationServiceImpl accountMovementsReturnBillValidationService) {
        this.accountMovementsReturnBillValidationService = accountMovementsReturnBillValidationService;
    }

    @Autowired
    public void setAccountMovementsReturnBillService(AccountMovementsReturnBillServiceImpl accountMovementsReturnBillService) {
        this.accountMovementsReturnBillService = accountMovementsReturnBillService;
    }

    @Autowired
    public void setAccountPayersService(AccountPayersServiceImpl accountPayersService) {
        this.accountPayersService = accountPayersService;
    }

    @Autowired
    public void setAccountBalanceService(AccountBalanceServiceImpl accountBalanceService) {
        this.accountBalanceService = accountBalanceService;
    }

    @Autowired
    public void setAliasService(AliasServiceImpl aliasService) {
        this.aliasService = aliasService;
    }

    @Autowired
    public void setCardMovementsDebitSplitService(CardMovementsDebitSplitServiceImpl cardMovementsDebitSplitService) {
        this.cardMovementsDebitSplitService = cardMovementsDebitSplitService;
    }

}