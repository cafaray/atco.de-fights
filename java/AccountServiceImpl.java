package com.idk.bs.service.accounts;

import static com.idk.bs.service.accounts.AccountsSOAPMessage.getAccountsListMessage;
import static com.idk.bs.utils.GlobalUtils.readFileAsString;
import static com.idk.bs.utils.XMLUtils.convertXMLToObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import javax.xml.bind.JAXBException;

import org.apache.commons.lang3.tuple.Pair;
import org.dozer.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ws.client.core.WebServiceTemplate;

import com.bs.cdsws.data.xsd.RequestHeader;
import com.bs.cdsws.product.common.containers.xsd.InterveningQueryI;
import com.bs.cdsws.product.common.services.cuinterveningquery.xsd.InterveningQueryIRequest;
import com.bs.cdsws.product.common.services.cuinterveningquery.xsd.InterveningQueryIResponse;
import com.everis.bs.model.accounts.InterveningQueryRequest;
import com.everis.bs.model.accounts.InterveningQueryResponse;
import com.everis.bs.model.accounts.enroll.AccountsListEnrollResponse;
import com.everis.bs.model.accounts.position.AccountsPositionResponse;
import com.everis.bs.utils.accounts.Extractor;
import com.everis.bs.utils.soapclient.SoapAdapter;
import com.idk.bs.app.config.AppProperties;
import com.idk.bs.app.exception.InternalServerErrorException;
import com.idk.bs.app.exception.NotFoundException;
import com.idk.bs.app.exception.SoapFaultException;
import com.idk.bs.model.AccountModel;
import com.idk.bs.model.BaseModel;
import com.idk.bs.model.accounts.AccountsListModelV1;
import com.idk.bs.service.BaseService;
import com.idk.bs.utils.GlobalUtils;
import com.idk.bs.web.accounts.AccountsForm;
import com.idk.bs.web.config.SessionBean;

/**
 * Account's service implementation.
 *
 * @author marcserra
 */
@Service
public class AccountsServiceImpl extends BaseService implements AccountsService {

    /**
     * CDS service declaration to get intervinents from an account.
     */
    private final static Pair<String, String> CU_INTERVENING_QUERY_INTERVENING_QUERY_I_SOAP = Pair.of("common.CUInterveningQuery?wsdl",
            "interveningQueryI");

    /**
     * Translation between models.
     */
    @Autowired
    private Mapper accountInterveningMapper;

    /**
     * Perform WS calls over SOAP.
     */
    @Autowired
    private SoapAdapter soapAdapter;

    /**
     * Old-style CDSWS name.
     */
    private static final String WS_NAME = "common.CUGetAccounts";

    /**
     * Old-style CDSWS operation.
     */
    private static final String SOAP_ACTION = "\"urn:getAccounts\"";

    /**
     * Old-style template path.
     */
    private final String templatePath;

    /**
     * Old-style SOAP client.
     */
    @Autowired
    private final WebServiceTemplate wsTemplate;

    /**
     * Constructor
     *
     * @param appProperties
     * @param wsTemplate
     */
    @Autowired
    public AccountsServiceImpl(AppProperties appProperties, WebServiceTemplate wsTemplate) {
        super(appProperties.getServicesUrl() + WS_NAME);
        this.wsTemplate = wsTemplate;
        this.templatePath = appProperties.getTemplatePath();
        this.fakeService = appProperties.isFakeRequest();
        this.fakeXmlName = "accountsNormal";
        this.fakeFolder = "accounts";

        try {
            this.xslSource = readFileAsString("xsl/accounts/accountsNormal.xsl");
        } catch (IOException ioe) {
            logger.logException(getClass(), ioe.getMessage());
        }
    }

    /**
     * @see AccountsService
     * @param form
     * @return
     * @throws SoapFaultException
     * @throws InternalServerErrorException
     * @throws NotFoundException
     */
    @Override
    public BaseModel getAccountsList(AccountsForm form) throws SoapFaultException, InternalServerErrorException, NotFoundException {
        String xmlResponse;
        AccountsListModelV1 modelResponse = null;

        try {
            // WS Call message
            String soapMessage = getAccountsListMessage(form);

            // Get the XML Response
            xmlResponse = super.getXmlResponse(wsTemplate, wsURL, soapMessage, SOAP_ACTION, new HashMap<>(), templatePath);

            // Convert to model object
            modelResponse = (AccountsListModelV1) convertXMLToObject(xmlResponse, AccountsListModelV1.class);

            // Filter results by Contract Code
            if (!GlobalUtils.stringIsEmpty(form.getContractCCC())) {

                List<AccountModel> filteredAccounts = new ArrayList<>();

                for (AccountModel account : modelResponse.getAccounts()) {

                    if (form.getContractCCC().replace("-", "").equals(account.getNumber().replace("-", ""))) {
                        filteredAccounts.add(account);
                    }
                }

                modelResponse.setAccounts((ArrayList<AccountModel>) filteredAccounts);
            }

            // Check NotFoundException
            if (modelResponse.getAccounts().isEmpty()) {
                throw new NotFoundException();
            }

        } catch (JAXBException e) {
            logger.logException(getClass(), e.getMessage());
            throw new InternalServerErrorException();
        }

        return modelResponse;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public AccountsPositionResponse getAccountsPosition(AccountsListModelV1 accountsList) throws Exception {
        return new Extractor().getAccountsPosition(accountsList);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public InterveningQueryResponse getInterveners(SessionBean sessionBean, InterveningQueryRequest restRequest) throws Exception {
        /* Input adaptation */
        InterveningQueryIRequest soapRequest = new InterveningQueryIRequest();
        soapRequest.setHeader(accountInterveningMapper.map(sessionBean, RequestHeader.class));
        soapRequest.setData(accountInterveningMapper.map(restRequest, InterveningQueryI.class));

        /* CDS call */
        InterveningQueryIResponse soapResponse = soapAdapter.call(SoapAdapter.SOAP_URL_HEADER.CDS, CU_INTERVENING_QUERY_INTERVENING_QUERY_I_SOAP,
                soapRequest, InterveningQueryIResponse.class);

        /* Output adaptation */
        return accountInterveningMapper.map(soapResponse.getData(), InterveningQueryResponse.class);
    }

	@Override
	public AccountsListEnrollResponse getAccountsEnroll(SessionBean sessionBean, AccountsListEnrollResponse restRequest)
			throws SoapFaultException, InternalServerErrorException, NotFoundException {
		return null;
	}

}