package com.idk.bs.service.accounts;

import static com.idk.bs.enums.AccountFilter.ACCOUNT;
import com.idk.bs.model.DateModel;
import static com.idk.bs.utils.GlobalUtils.stringIsEmpty;
import com.idk.bs.web.accounts.AccountsForm;
import com.idk.bs.web.config.SessionBean;
import com.idk.bs.web.accounts.AccountMovementsForm;

/**
 *
 * @author marcserra
 */
public class AccountsSOAPMessage {

    /**
     * SOAP message for common.CUGetAccounts webservice
     *
     * @param form
     * @return String containing the message
     */
    public static String getAccountsListMessage(AccountsForm form) {
        StringBuilder soapMsg = new StringBuilder();

        String type = (stringIsEmpty(form.getType())) ? ACCOUNT.toString() : form.getType();

        soapMsg.append("<cug:getAccounts xmlns:cug=\"http://cugetaccounts.services.common.product.cdsws.bs.com\" ")
                .append("xmlns:xsd=\"http://cugetaccounts.services.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd1=\"http://containers.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd2=\"http://data.cdsws.bs.com/xsd\">")
                .append("<cug:request>")
                .append("<xsd:data>")
                .append("<xsd1:accountType>").append(type).append("</xsd1:accountType>")
                .append("</xsd:data>")
                .append("<xsd:header>")
                .append("<xsd2:product>").append(form.getProduct()).append("</xsd2:product>")
                .append("<xsd2:sessionId>").append(form.getSessionId()).append("</xsd2:sessionId>")
                .append("</xsd:header>")
                .append("</cug:request>")
                .append("</cug:getAccounts>");

        return soapMsg.toString();
    }

    /**
     * SOAP message for common.CUMovilExtractQuery webservice
     *
     * @param form
     * @return String containing the message
     */
    public static String getAccountMovementsMessage(AccountMovementsForm form) {
        StringBuilder soapMsg = new StringBuilder();

        DateModel dateFrom = new DateModel(form.getDateFrom());
        DateModel dateTo = new DateModel(form.getDateTo());

        soapMsg.append("<cum:accountDataToQuery xmlns:cum=\"http://cumovilextractquery.services.common.product.cdsws.bs.com\" ")
                .append("xmlns:xsd=\"http://cumovilextractquery.services.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd1=\"http://containers.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd2=\"http://datatypes.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd3=\"http://data.cdsws.bs.com/xsd\">")
                .append("<cum:request>")
                .append("<xsd:data>")
                .append("<xsd1:orderAccount>")
                .append("<xsd2:accountNumber>").append(form.getAccount().getAccountNumber()).append("</xsd2:accountNumber>")
                .append("<xsd2:bank>").append(form.getAccount().getBank()).append("</xsd2:bank>")
                .append("<xsd2:branch>").append(form.getAccount().getBranch()).append("</xsd2:branch>")
                .append("<xsd2:checkDigit>").append(form.getAccount().getCheckDigit()).append("</xsd2:checkDigit>")
                .append("</xsd1:orderAccount>");
        if (!form.isMoreRequest()) {
            soapMsg.append("<xsd1:dateMovFrom>")
                    .append("<xsd2:day>").append(dateFrom.getDay()).append("</xsd2:day>")
                    .append("<xsd2:month>").append(dateFrom.getMonth()).append("</xsd2:month>")
                    .append("<xsd2:year>").append(dateFrom.getYear()).append("</xsd2:year>")
                    .append("</xsd1:dateMovFrom>")
                    .append("<xsd1:dateMovTo>")
                    .append("<xsd2:day>").append(dateTo.getDay()).append("</xsd2:day>")
                    .append("<xsd2:month>").append(dateTo.getMonth()).append("</xsd2:month>")
                    .append("<xsd2:year>").append(dateTo.getYear()).append("</xsd2:year>")
                    .append("</xsd1:dateMovTo>");
        }
        soapMsg.append("</xsd:data>")
                .append("<xsd:header>")
                .append("<xsd3:product>").append(form.getProduct()).append("</xsd3:product>")
                .append("<xsd3:sessionId>").append(form.getSessionId()).append("</xsd3:sessionId>")
                .append("</xsd:header>")
                .append("</cum:request>")
                .append("</cum:accountDataToQuery>");

        return soapMsg.toString();
    }
    
    /**
     * SOAP message for common.IPGetAccounts webservice
     *
     * @param SessionBean
     * @return String containing the message
     */
    public static String getAccountsEnrollMessage(SessionBean session) {
        StringBuilder soapMsg = new StringBuilder();

        soapMsg.append("<ipg:start xmlns:ipg=\"http://ipgetaccounts.services.common.product.cdsws.bs.com\" ")
                .append("xmlns:xsd=\"http://ipgetaccounts.services.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd1=\"http://containers.common.product.cdsws.bs.com/xsd\" ")
                .append("xmlns:xsd2=\"http://data.cdsws.bs.com/xsd\">")
                .append("<ipg:request>")
                .append("<xsd:header>")
                .append("<xsd2:product>").append(session.getProduct()).append("</xsd2:product>")
                .append("<xsd2:sessionId>").append(session.getSessionId()).append("</xsd2:sessionId>")
                .append("</xsd:header>")
                .append("</ipg:request>")
                .append("</ipg:start>");

        return soapMsg.toString();
    }
}