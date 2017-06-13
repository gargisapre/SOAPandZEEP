import zeep

wsdl = 'http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl'
client = zeep.Client(wsdl=wsdl)

login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=2, loginId='test', password='isdn1')

CSName = client.get_type('ns0:childSupportName')
test_name = CSName(searchExactName=False, firstName="TEST", lastName="EXAMPLE", fromDate='09/01/1992', toDate='12/10/2016')
test_name2 = CSName(searchExactName=True, firstName="KAREN", lastName="KANE", fromDate='09/01/1992', toDate='12/10/2016')

nameList = [test_name, test_name2]

childSupportOrder = client.get_type('ns0:childSupportOrder')

patriotOrder = client.get_type('ns0:patriotOrder')

stateWideLienOrder = client.get_type('ns0:stateWideLienOrder')
test_sWLO = stateWideLienOrder(deliveryMethod='Web', reference='JEREMY', vendorId=9999)

print(client.service.login(log_in))
#client.service.logout()
print(client.service.getStateWideLienEffectiveDate())

i = 99
test_CSO = childSupportOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference='AA TEST', vendorId=i, name=nameList )
print(client.service.submitChildSupport(test_CSO))

test_Patriot =  patriotOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference='AA TEST', vendorId=i, name=nameList )
print(client.service.submitPatriot(test_Patriot))

client.service.logout()