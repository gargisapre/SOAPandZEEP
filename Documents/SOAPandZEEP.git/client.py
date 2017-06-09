import zeep

wsdl = 'http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl'
client = zeep.Client(wsdl=wsdl)


a = client.service.validate('test', 0)