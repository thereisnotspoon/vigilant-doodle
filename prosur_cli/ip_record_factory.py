import dbconn

#obtiene una lista python con todos los signos distintivos
def obtenerSignosDistintivos():
    signosProcesados = []
    signos = dbconn.consultarSignos()
    for signo in signos:
        signo = construirSignoDistintivo(signo)
        signosProcesados.append(signo)
    return signosProcesados

#obtiene una lista python con todos las patentes de diseño
def obtenerPatentesDisenio():
    patentesProcesadas = []
    patentes = dbconn.consultarPatentesDisenio()
    for patente in patentes:
        patente = construirPatenteDisenio(patente)
        patentesProcesadas.append(patente)
    return patentesProcesadas 

#obtiene una lista python con todos las patentes de invencion 
def obtenerPatentesInvencion():
    patentesProcesadas = []
    patentes = dbconn.consultarPatentesInvencion()
    for patente in patentes:
        patente = construirPatenteInvencion(patente)
        patentesProcesadas.append(patente)
    return patentesProcesadas

#relaciona un signo distintivo  con su File Data y sus clases 
#de niza, y retorna los datos como un diccionario
def construirSignoDistintivo(signo):
    signo = agregarFileData(signo)
    signo = agregarNizas(signo)
    return signo 

#relaciona una patente de diseño con sus prioridades
#retorna el conjunto de datos como un solo diccionario
def construirPatenteDisenio(patenteDisenio):
    patenteDisenio = agregarFileData(patenteDisenio)
    patenteDisenio = agregarPrioridades(patenteDisenio) 
    return patenteDisenio

#relaciona una patente de invencion con sus prioridades
#retorna el conjunto de datos como un solo diccionario
def construirPatenteInvencion(patenteInvencion):
    patenteInvencion = agregarFileData(patenteInvencion)
    patenteInvencion = agregarPrioridades(patenteInvencion) 
    return patenteInvencion
    
#retorna un diccionario que contiene datos tanto de un ipRecord
#como de sus FileData asociados
def agregarFileData(ipRecord):
    filedata = dbconn.consultarFileData(ipRecord["ip_record_id"])
    ipRecord = dict(ipRecord)
    ipRecord["filedata"] = []
    for fd in filedata:
        fd = dict(fd)
        ipRecord["filedata"].append(fd)
    return ipRecord

#retorna un diccionario que contiene datos tanto de un ipRecord
#como de sus clases de niza asociadas
def agregarNizas(ipRecord):
    niceclasses = dbconn.consultarNizas(ipRecord["ip_record_id"])
    ipRecord = dict(ipRecord)
    ipRecord["niceclasses"] = []
    for nc in niceclasses:
        nc = dict(nc)
        ipRecord["niceclasses"].append(nc)
    return ipRecord

#retorna un diccionario que contiene datos tanto de un ipRecord
#como de sus prioridades asociadas
def agregarPrioridades(ipRecord):
    prioridades = dbconn.consultarPrioridades(ipRecord["ip_record_id"])
    ipRecord = dict(ipRecord)
    ipRecord["prioridades"] = []
    for pr in prioridades:
        pr = dict(pr)
        ipRecord["prioridades"].append(pr)
    return ipRecord

def main():
    signs = obtenerSignosDistintivos()
    
    for sign in signs:
        print(sign, "\n\n")

if __name__ == "__main__":
    main()
