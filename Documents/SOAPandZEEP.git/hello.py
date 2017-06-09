import zeep

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
# client = zeep.Client(wsdl=wsdl)
# print(client.service.Method1('Zeep', 'is cool'))

from zeep import Client
from zeep import xsd

client = Client('http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl')


