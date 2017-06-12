import zeep

wsdl = 'http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl'
client = zeep.Client(wsdl=wsdl)

login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=2, loginId='test', password='isdn1')

CSName = client.get_type('ns0:childSupportName')
test_name = CSName(searchExactName='False', firstName="TEST", lastName="EXAMPLE", fromDate='01/01/2010', toDate='01/01/2017')

nameList = [test_name]

childSupportOrder = client.get_type('ns0:childSupportOrder')
test_CSO = childSupportOrder(deliveryMethod='Email', deliveryInfo='JZhang@signatureinfo.com', vendorId=2, clientFirmNumber='1234', name=nameList )

stateWideLienOrder = client.get_type('ns0:stateWideLienOrder')
test_sWLO = stateWideLienOrder(deliveryMethod='Web', reference='JEREMY', vendorId=9999)

print(client.service.login(log_in))
print(client.service.getStateWideLienEffectiveDate())
print(client.service.submitChildSupport(test_CSO))


client.service.logout()