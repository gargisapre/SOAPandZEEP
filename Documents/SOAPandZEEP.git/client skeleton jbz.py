import zeep
import openpyxl

select = 2   #0 = alalnsis, 1 = dev, 2 = test
endpoint = ['http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl',
            'http://sis-jas-dev.risk.regn.net:8080/ws/signon?wsdl',
            'http://sis-jas-test.risk.regn.net:8080/ws/signon?wsdl']
wsdl = endpoint[select]
client = zeep.Client(wsdl=wsdl)

login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=2, loginId='test', password='isdn1')

CSName = client.get_type('ns0:childSupportName')
test_name  = CSName(searchExactName=False, firstName="LOREEN", lastName="DOE", fromDate='09/01/1992', toDate='08/01/2016')
test_name2 = CSName(searchExactName=False, firstName="KAREN", lastName="CANE", fromDate='09/01/1992', toDate='08/01/2016')
test_name3 = CSName(searchExactName=False, firstName="JANE", lastName="BRAUN", fromDate='09/01/1992', toDate='08/01/2016')

names = [test_name, test_name2, test_name3]
nameList = [names[select]]

childSupportOrder = client.get_type('ns0:childSupportOrder')
patriotOrder = client.get_type('ns0:patriotOrder')
lienOrder = client.get_type('ns0:stateWideLienOrder')
tideOrder = client.get_type('ns0:tidelandOrder')

print(client.service.login(log_in))
#client.service.logout()
print(client.service.getStateWideLienEffectiveDate())

ref = ['A_PYTHON', 'D_PYTHON', 'T_PYTHON']

i = 99
test_CSO = childSupportOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference=ref[select]+'_CSO', vendorId=i, name=nameList )

test_Patriot =  patriotOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference=ref[select]+'_PT',  vendorId=i, name=nameList )

test_SWLO =        lienOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                         reference=ref[select]+'_LO',  vendorId=i, name=nameList )

test_TLO =         tideOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                         reference=ref[select]+'_TLO', vendorId=i, county='CUMBERLAND',
	                         block=1, lot=1, municipality='GREENWICH', municipalityType='TOWNSHIP',
	                         owner='JOHN KANE', state='NJ', hasGrantPackagePricing=True, isGrantRequested=True)

#print(client.service.submitPatriot(test_Patriot)) #test submitPatriot
#print(client.service.submitChildSupport(test_CSO)) #test submitChildSupport
#print(client.service.submitStateWideLien(test_SWLO)) #test submitStateWideLien
print(client.service.submitTideland(test_TLO))
print(client.service.submit)
client.service.logout()