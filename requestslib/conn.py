import contextlib
import OpenSSL.crypto
import os
import requests
import ssl
import tempfile
from lxml import etree
from requests import Session
#zeep imports
from zeep import Client
from zeep.transports import Transport

@contextlib.contextmanager
def pfx_to_pem(pfx_path, pfx_password):
    ''' Decrypts the .pfx file to be used with requests. '''
    with tempfile.NamedTemporaryFile(suffix='.pem') as t_pem:
        f_pem = open(t_pem.name, 'wb')
        pfx = open(pfx_path, 'rb').read()
        p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)
        f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
        f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
        ca = p12.get_ca_certificates()
        if ca is not None:
            for cert in ca:
                f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
        f_pem.close()
        yield t_pem.name

import logging.config

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

# HOW TO USE:
url = 'https://10.5.2.12:8443/ProsurCatalog/ProsurIPRecordWS?wsdl'
with pfx_to_pem('clientEC.pfx', 'Ea6@3H') as cert:
    #r = requests.get(url, cert=cert, verify=False, timeout=None)
    #print(r.text)
    #print(r)

    session = Session()
    session.verify = False
    session.cert = cert
    transport = Transport(session=session)
    client = Client(
        url, 
        transport=transport
    )
    
    file1 = {
        'fileName':'test-file',
        'fileTitle':'test-title',
        'fileDescription':'test-description'
    }

    niceClass = {'niceClass':11, 'activity':'anti-dazzle anti-splash'}

    dsign = {
        'distinctiveSignType':'MARCA',
        'expiration':'2021-06-20-03:00',
        'logoDescription':'lorem ipsum consequat imperdiet duis',
        'niceClasses':[niceClass],
        'registrationDate':'2005-05-26',
    }

    ipRecord = {
        'ipRecordId':'3302',
        'onapiId':'PY',
        'applicationId':'1706136665488629998',
        'recordType':'DISTINCTIVE_SIGN',
        'nationalPresentationDate':'2017-12-12',
        'nationalPublishingDate':'2017-12-12',
        'title':'Dummy Title',
        'applicantName':['Juan Maria Chipugsi','Bill Gates'],
        'statusId':'EN_TRAMITE',
        #'ipRecordDetailLink':'http://www.example.com',
        'ipRecordFilesService':'http://192.168.1.37:8080/ProsurOfficeWS/IPOfficeWS',
        'files':[file1],
        #'distinctiveSignType':'MARCA',
        #'expiration':'2021-06-20-03:00',
        #'logoDescription':'lorem ipsum consequat imperdiet duis',
        #'niceClasses':[niceClass],
        #'registrationDate':'2005-05-26',
        #'trigger':'afd;',
        
        
    }

    ipr_type = client.get_type('ns0:ipRecord')
    ipRecordDS = ipr_type(
        ipRecordId = '3302',
        onapiId = 'PY',
        applicationId = '1706136665488629998',
        recordType = 'DISTINCTIVE_SIGN',
        nationalPresentationDate = '2017-12-12',
        nationalPublishingDate = '2017-12-12',
        title = 'Dummy Title',
        applicantName = ['Juan Maria Chipugsi','Bill Gates'],
        statusId = 'EN_TRAMITE',
        #ipRecordDetailLink = 'http://www.example.com',
        ipRecordFilesService = 'http://192.168.1.37:8080/ProsurOfficeWS/IPOfficeWS',
        files = [file1]
    )
    #print(dir(ipRecordDS))

    ds_type = client.get_type('ns0:distinctiveSign')
    ds_type.extend(ipr_type)
    ds = ds_type(
        #ipRecordId = '3302',
        onapiId = 'EC',
        applicationId = '1706136665488629998',
        recordType = 'DISTINCTIVE_SIGN',
        nationalPresentationDate = '2017-12-12',
        nationalPublishingDate = '2017-12-12',
        title = 'Dummy Title',
        applicantName = ['Juan Maria Chipugsi','Bill Gates'],
        statusId = 'EN_TRAMITE',
        ipRecordDetailLink = 'http://www.example.com',
        ipRecordFilesService = 'http://192.168.1.37:8080/ProsurOfficeWS/IPOfficeWS',
        files = [file1],
        distinctiveSignType = 'MARCA',
        expiration = '2021-06-20-03:00',
        logoDescription = 'lorem ipsum consequat imperdiet duis',
        niceClasses = [niceClass],
        registrationDate = '2005-05-26'
        #'trigger':'afd;',
    )

    
    user = 'ecu_usr'
    
    #uncomment nxtlns to see the soap message to send as xml
    node = client.create_message(client.service, 'getRecord', ipRecord=ds, user=user)    
    print(etree.tostring(node, pretty_print=True))
 
    #rec = client.service.getRecord(ipRecord,user)
    rec = client.service.createRecord(ds, user)
    
    #trying to see the methods of the response object
    print(dir(rec.ipRecordId))

    print(rec.ipRecordId)
    
    print(type(rec))
     
    for attr in rec:
        print(attr)
    
    
    

