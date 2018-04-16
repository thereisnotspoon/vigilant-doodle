import prosur_cli.ws_helpers as ws_helpers
import prosur_cli.log_mod as log_mod


def createDesignPatent(d_patent):
    client = ws_helpers.obtenerClienteWS()
    # obtencion el tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')
    # obtencion del tipo de objeto designPatent 
    designPatentType = client.get_type('ns0:designPatent')
    # extension del tipo ipRecord a designPatent
    designPatentType.extend(ipRecordType)
    # llenado de  datos en una patente de diseño a enviar
    patente = designPatentType(
        #datos generales de la patente
        onapiId                 =   d_patent["onapiid"],
        applicationId           =   d_patent["applicationid"],
        recordType              =   d_patent["recordtype"],
        nationalPresentationDate=   d_patent["nationalpresentationdate"],
        nationalPublishingDate  =   d_patent["nationalpublishingdate"],
        title                   =   d_patent["title"],
        applicantName           =   d_patent["applicantname"],
        statusId                =   d_patent["statusid"],
        ipRecordDetailLink      =   d_patent["iprecorddetaillink"],
        files                   =   d_patent["filedata"],
        ipRecordFilesService    =   d_patent["iprecordfilesservice"],
        #datos específicos de una patente
        patentAbstract          =   d_patent["patentabstract"],
        description             =   d_patent["description"],
        requestCountryId        =   d_patent["requestcountryid"],
        representativeName      =   d_patent["representativename"],
        registrationNumber      =   d_patent["registrationnumber"],
        conclusionMethod        =   d_patent["conclusionmethod"],
        inventors               =   d_patent["inventors"],
        technicalReportDetail   =   d_patent["technicalreportdetail"],
        #datos específicos de una patente de diseño
        designClassification    =   d_patent["designclassification"],
        mainDesignImage         =   d_patent["maindesignimage"],
        locarnoClassification   =   d_patent["locarnoclassification"]

    )

    user = "ecu_user"
    #impresion del mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "getRecord",patente, user)
    #client.service.createRecord(signo, user)
    return 

def createInventionPatent(i_patent):
    client = ws_helpers.obtenerClienteWS()
    # obtencion del tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')
    # obtencion del tipo de objeto inventionPatent 
    inventionPatentType = client.get_type('ns0:inventionPatent')
    # extencion del tipo ipRecord a inventionPatent
    inventionPatentType.extend(ipRecordType)
    # llenado de  datos en una patente de invención a enviar
    patente = inventionPatentType(
        #datos generales de la patente
        onapiId                     =   i_patent["onapiid"],
        applicationId               =   i_patent["applicationid"],
        recordType                  =   i_patent["recordtype"],
        nationalPresentationDate    =   i_patent["nationalpresentationdate"],
        nationalPublishingDate      =   i_patent["nationalpublishingdate"],
        title                       =   i_patent["title"],
        applicantName               =   i_patent["applicantname"],
        statusId                    =   i_patent["statusid"],
        ipRecordDetailLink          =   i_patent["iprecorddetaillink"],
        files                       =   i_patent["filedata"],
        ipRecordFilesService        =   i_patent["iprecordfilesservice"],
        #datos específicos de una patente
        patentAbstract              =   i_patent["patentabstract"],
        description                 =   i_patent["description"],
        requestCountryId            =   i_patent["requestcountryid"],
        representativeName          =   i_patent["representativename"],
        registrationNumber          =   i_patent["registrationnumber"],
        conclusionMethod            =   i_patent["conclusionmethod"],
        inventors                   =   i_patent["inventors"],
        technicalReportDetail       =   i_patent["technicalreportdetail"],
        #datos específicos de una patente de invención 
        patentTypeId                =   i_patent["patenttypeid"],
        internationalClassification =   i_patent["internationalclassification"],
        pctApplicationNumber        =   i_patent["pctapplicationnumber"],
        pctApplicationDate          =   i_patent["pctapplicationdate"]

    )

    user = "ecu_user"
    #imprimir el mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "getRecord", patente, user)
    #client.service.createRecord(signo, user)
    return 

def createDistinctiveSign(sign):
    client = ws_helpers.obtenerClienteWS()
    # obtencion del tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')
    # obtencion del tipo de objeto disticntiveSign
    distinctiveSignType = client.get_type('ns0:distinctiveSign')
    # extencion del tipo ipRecord a distinctiveSign
    distinctiveSignType.extend(ipRecordType)
    
    # llenado datos en un signo distintivo a enviar
    d_sign = distinctiveSignType(
        #datos generales de la patente
        onapiId                 =   sign.get("onapiid", "EC"),
        applicationId           =   sign.get("applicationid", "999999999"),
        recordType              =   sign.get("recordtype", "DISTINCTIVE_SIGN"),
        nationalPresentationDate=   sign.get("nationalpresentationdate", "2017-12-12"),
        nationalPublishingDate  =   sign.get("nationalpublishingdate", "2017-12-12"),
        title                   =   sign.get("title"),
        applicantName           =   sign.get("applicantname", "BOB"),
        statusId                =   sign.get("statusid", "EN_TRAMITE"),
        ipRecordDetailLink      =   sign.get("iprecorddetaillink", "http://iepi.aunnoexiste.gob"),
        files                   =   sign.get("filedata", []),
        ipRecordFilesService    =   sign.get("iprecordfilesservice", "http://iepi.aunnoexiste.gob"),
        #datos específicos de un signo distintivo 
        distinctiveSignType     =   sign["distinctivesigntype"],
        presentationType        =   sign.get("presentationtype", ""),
        registrationDate        =   sign["registrationdate"],
        expiration              =   sign["expiration"],
        #niceClasses             =   sign["niceclasses"],
        logoDescription         =   sign["logodescription"]
    )

    user = "ecuador_user"
    #impresion del mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "createRecord", d_sign, user)
    #client.service.createRecord(d_sign, user)
    return


