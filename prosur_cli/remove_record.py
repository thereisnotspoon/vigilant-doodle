import prosur_cli.ws_helpers as ws_helpers
import prosur_cli.log_mod as log_mod

def removeRecord(sign):
    client = ws_helpers.obtenerClienteWS()
    # obtencion del tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')

    # construccion de un ipRecord con los datos necesarios para la eliminacion 
    ip_record = ipRecordType(
        onapiId                 =   sign.get("onapiid", ""),
        applicationId           =   sign.get("applicationid", ""),
        recordType              =   sign.get("recordtype", ""),
    )

    user = "ecuador_user"
    #impresion del mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "removeRecord", ip_record, user)
    client.service.removeRecord(ip_record, user)
    return

def removeRecordById(ipRecordId):
    client = ws_helpers.obtenerClienteWS()
    # obtencion del tipo de objeto ipRecord
    ipRecordType = client.get_type('ns0:ipRecord')

    # construccion de un ipRecord con los datos necesarios para la eliminacion 
    ip_record = ipRecordType(
        ipRecordId = ipRecordId
    )

    user = "ecuador_user"
    #impresion del mensaje SOAP a ser enviado
    log_mod.imprimirMensajeSOAP(client, "removeRecord", ip_record, user)
    client.service.removeRecord(ip_record, user)
    return
