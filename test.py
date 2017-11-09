import zeep
from lxml import etree

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
node = client.create_message(client.service, 'Method1', bstrParam1='hi',bstrParam2='hi2')

print(etree.tostring(node, pretty_print=True))

with client.options(raw_response=True):
    response = client.service.Method1('Hello', 'zeep')

    #response is now a regular requests.Response object
    assert response.status_code == 200
    assert response.content

#print(client.service.Method1('Zeep', 'sucks'))
