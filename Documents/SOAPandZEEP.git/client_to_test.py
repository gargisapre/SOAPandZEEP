import zeep

wsdl = 'http://sis-jas-test.risk.regn.net:8080/ws/signon?wsdl'
client = zeep.Client(wsdl=wsdl)

login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=2, loginId='test', password='isdn1')

CSName = client.get_type('ns0:childSupportName')
test_name  = CSName(searchExactName=False, firstName="LOREEN", lastName="DOE", fromDate='09/01/1992', toDate='08/01/2016')
test_name2 = CSName(searchExactName=False, firstName="KAREN", lastName="CANE", fromDate='09/01/1992', toDate='08/01/2016')
test_name3 = CSName(searchExactName=False, firstName="JANE", lastName="BROWN", fromDate='09/01/1992', toDate='08/01/2016')

nameList = [test_name3]

childSupportOrder = client.get_type('ns0:childSupportOrder')

patriotOrder = client.get_type('ns0:patriotOrder')

stateWideLienOrder = client.get_type('ns0:stateWideLienOrder')
test_sWLO = stateWideLienOrder(deliveryMethod='Web', reference='JEREMY', vendorId=99)

print(client.service.login(log_in))
#client.service.logout()
print(client.service.getStateWideLienEffectiveDate())

i = 99
test_CSO = childSupportOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference='T_PYTHON', vendorId=i, name=nameList )
print(client.service.submitChildSupport(test_CSO))

test_Patriot =  patriotOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference='T_PYTHON', vendorId=i, name=nameList )
print(client.service.submitPatriot(test_Patriot))

client.service.logout()