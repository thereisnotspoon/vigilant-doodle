#importacion para obtener informacion de depuracion
#a saber: los archivos soap de peticion y respuesta
import logging.config
from lxml import etree

#diccionario de configuracion requerido para imprimir los logs
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

def imprimirMensajeSOAP(client, metodo, ipRecord, user="ecu_user"):
    #las sig 2 lineas estan tienen el fin de imprimir informacion de depuracion
    #en especifico, el mensaje soap por ser enviado
    node = client.create_message(client.service, metodo, ipRecord=ipRecord, user=user)
    print(etree.tostring(node, pretty_print=True).decode("UTF-8"))
