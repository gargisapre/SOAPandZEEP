import zeep
wsdl = 'http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl'
client = zeep.Client(wsdl=wsdl)
login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=2, loginId='test', password='isdn1')
child_support_name = client.get_type('ns0:childSupportName')
csName = child_support_name(searchExactName='False', firstName="hello", lastName="world", fromDate='01/03/1997', toDate='03/04/1997')

nameList = [csName]

child_Support_Order = client.get_type('ns0:childSupportOrder')
csOrder = child_Support_Order(deliveryMethod='Email', deliveryInfo='gargisapre@gmail.com', vendorId=2, clientFirmNumber='9999', name=nameList )


state_Wide_Lien_Order = client.get_type('ns0:stateWideLienOrder')
sWLO = state_Wide_Lien_Order(deliveryMethod='Web', reference='Gargi', vendorId=9999)

patriot_name = client.get_type('ns0:patriotName')
pName = patriot_name(searchExactName='False',firstName='hello',lastName='World',fromDate='01/03/1997',toDate='03/04/1997')
nameList2=[pName]

patriot_order = client.get_type('ns0:patriotOrder')
pOrder = patriot_order(deliveryMethod='Email', deliveryInfo='gargisapre@gmail.com', vendorId=2, clientFirmNumber='9999', name=nameList2)

print(client.service.login(log_in)) 
a = client.service.validate('test', 0)
print(a)

print(client.service.submitChildSupport(csOrder))
print(client.service.getStateWideLienEffectiveDate())
print(client.service.submitPatriot(pOrder))
# print(client.service.submitStateWideLien(sWLO))
client.service.logout()
