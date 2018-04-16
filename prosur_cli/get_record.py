import prosur_cli.ws_helpers as ws_helpers
import prosur_cli.log_mod as log_mod

def getRecord(onapiId, applicationId, recordType):
    client = ws_helpers.obtenerClienteWS()
    # obtencion del tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')

    # construccion de un ipRecord con los datos necesarios para la consulta 
    ip_record = ipRecordType(
        onapiId                 =   onapiId,
        applicationId           =   applicationId,
        recordType              =   recordType,
    )

    user = "ecuador_user"
    #impresion del mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "getRecord", ip_record, user)
    client.service.getRecord(ip_record, user)
    return

def getRecordById(ipRecordId):
    client = ws_helpers.obtenerClienteWS()
    # obtencion del tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')

    # construccion de un ipRecord con los datos necesarios para la consulta 
    ip_record = ipRecordType(
        ipRecordId = ipRecordId
    )

    user = "ecuador_user"
    #impresion del mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "getRecord", ip_record, user)
    client.service.getRecord(ip_record, user)
    return



