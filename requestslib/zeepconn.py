from requests import Session
from zeep import Client
from zeep.transports import Transport

wsdl = 'https://10.5.2.12:8443/ProsurCatalog/ProsurIPRecordWS?wsdl'

session = Session()
session.verify = False
transport = Transport(session=session)
client = Client(
    wsdl, 
    transport=transport)
