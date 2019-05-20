package com.idk.bs.service.accounts;

import static com.idk.bs.service.accounts.AccountsSOAPMessage.getAccountMovementsMessage;
import static com.idk.bs.utils.GlobalUtils.readFileAsString;
import static com.idk.bs.utils.XMLUtils.convertXMLToObject;
import static org.springframework.context.i18n.LocaleContextHolder.getLocale;

import java.io.IOException;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;
import org.springframework.ws.client.core.WebServiceTemplate;

import com.everis.bs.model.GenericGroupedMovementResponse;
import com.everis.bs.utils.accounts.Extractor;
import com.idk.bs.app.config.AppProperties;
import com.idk.bs.app.exception.InternalServerErrorException;
import com.idk.bs.app.exception.SoapFaultException;
import com.idk.bs.model.BaseModel;
import com.idk.bs.model.accounts.AccountMovementsListModel;
import com.idk.bs.service.BaseService;
import com.idk.bs.web.accounts.AccountMovementsForm;

/**
 *
 * @author marcserra
 */
@Service
public class AccountMovementsServiceImpl extends BaseService implements AccountMovementsService {

    private static final String WS_NAME = "common.CUMovilExtractQuery";
    private static final String SOAP_ACTION = "\"urn:accountDataToQuery\"";

    private final String templatePath;

    @Autowired
    private final WebServiceTemplate wsTemplate;

    /**
     * Constructor
     *
     * @param appProperties
     * @param wsTemplate
     */
    @Autowired
    public AccountMovementsServiceImpl(AppProperties appProperties, WebServiceTemplate wsTemplate) {
        super(appProperties.getServicesUrl() + WS_NAME);
        this.wsTemplate = wsTemplate;
        this.templatePath = appProperties.getTemplatePath();
        this.fakeService = appProperties.isFakeRequest();
        this.fakeXmlName = "accountMovements";
        this.fakeFolder = "accounts";

        try {
            this.xslSource = readFileAsString("xsl/accounts/accountMovements.xsl");
        } catch (IOException ioe) {
            logger.logException(getClass(), ioe.getMessage());
        }
    }

    /**
     * @see AccountMovementsService
     * @param form
     * @param isCompany
     * @return
     * @throws SoapFaultException
     * @throws InternalServerErrorException
     */
    @Override
    public BaseModel getAccountMovements(AccountMovementsForm form, boolean isCompany) throws SoapFaultException, InternalServerErrorException {
        String xmlResponse;
        AccountMovementsListModel modelResponse = null;

        try {
            // WS Call message
            String soapMessage = getAccountMovementsMessage(form);

            String xmlPath = "";

            // Get the XML Response
            switch (getLocale().getLanguage()) {
                case "ca":
                    xmlPath = "xml/accounts/accConceptDetail_ca.xml";
                    break;
                case "en":
                    xmlPath = "xml/accounts/accConceptDetail_en.xml";
                    break;
                case "es":
                    xmlPath = "xml/accounts/accConceptDetail_es.xml";
                    break;
                case "va":
                    xmlPath = "xml/accounts/accConceptDetail_va.xml";
                    break;
                default:
                    xmlPath = "xml/accounts/accConceptDetail_es.xml";
            }

            Map params = new HashMap<>();
            params.put("xmlPath", new ClassPathResource(xmlPath).getFile().getAbsolutePath());
            params.put("isCompany", isCompany);
            Calendar cal = Calendar.getInstance();
            params.put("currentDay", String.valueOf(cal.get(Calendar.DAY_OF_MONTH)));
            params.put("currentMonth", String.valueOf(cal.get(Calendar.MONTH) + 1));
            params.put("currentYear", String.valueOf(cal.get(Calendar.YEAR)));
            xmlResponse = super.getXmlResponse(wsTemplate, wsURL, soapMessage, SOAP_ACTION, params, templatePath);

            // Convert to model object
            modelResponse = (AccountMovementsListModel) convertXMLToObject(xmlResponse, AccountMovementsListModel.class);

            // Set product in form account
            form.getAccount().setProduct(modelResponse.getAccount().getProduct());

            // Set account
            modelResponse.setAccount(form.getAccount());

            // Set balance
            if (!modelResponse.getAccountMovements().isEmpty()) {
                modelResponse.getAccount().setAmount(modelResponse.getAccountMovements().get(0).getBalance());
            }

        } catch (SoapFaultException se) {
            if (se.getModel().getErrorMessage().contains("Z11421")) {
                // return an empty movements list with their account
                modelResponse = new AccountMovementsListModel();
                modelResponse.setAccount(form.getAccount());
                return modelResponse;
            } else {
                throw se;
            }
        } catch (InternalServerErrorException e) {
            throw e;
        } catch (Exception e) {
            logger.logException(getClass(), e.getMessage());
            throw new InternalServerErrorException();
        }

        return modelResponse;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public GenericGroupedMovementResponse getAccountMovementsListGroup(AccountMovementsListModel accountMovementsListModel) throws Exception {
        return new Extractor().getAccountMovementsListGroup(accountMovementsListModel);
    }

}