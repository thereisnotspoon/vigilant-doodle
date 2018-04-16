import os
import requests
from requests import Session

#zeep imports
from zeep import Client
from zeep.transports import Transport

import prosur_cli.ssl_context as ssl_context


#ruta de el archivo wsdl
url = '/home/archie/prosur-project/prosur/prosurc/prosur_cli/ProsurIPRecordWS.wsdl'

def obtenerClienteWS():
    """Retorna un objeto cliente, este sirve como un manejador que permite llamar
    a los metodos del IPRECORDWS"""
    path_to_pfx = "/home/archie/prosur-project/prosur/prosurc/prosur_cli/clientEC.pfx"
    #con el certificado adecuado se ejecutaran las subsecuentes instrucciones
    with ssl_context.pfx_to_pem(path_to_pfx, 'Ea6@3H') as cert:
        #crea una sesión 
        session = Session()
        #deshabilitar la verificación SSL
        session.verify = False
        session.cert = cert
        transport = Transport(session=session)
        #el objeto cliente que permite interactuar con el WS
        client = Client(
            url, 
            transport=transport
        )

        return client

def obtenerTipo(tipo):
    """ Recibe como parámetro una cadena de texto y devuelve una
        estructura de datos del tipo de IPRecord = tipo 
    """
    pass


