import zeep

wsdl = 'http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl'
client = zeep.Client(wsdl=wsdl)

login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=2, loginId='test', password='isdn1')

leinName = client.get_type('ns0:stateWideLienName')
test_name = leinName(SearchExactName='False', )

stateWideLienOrder = client.get_type('ns0:stateWideLienOrder')
test_sWLO = stateWideLienOrder(deliveryMethod='Email', deliveryInfo='JZhang@signatureinfo.com', reference='AMIT', vendorId=9999,
                                )

     ns0:stateWideLienOrder(appendToConfirmationNumber: xsd:string, clientFirmNu
mber: xsd:string, deliveryInfo: xsd:string, deliveryMethod: xsd:string, entryUse
r: xsd:string, name: ns0:stateWideLienName[], parentConfirmationNumber: xsd:stri
ng, reference: xsd:string, source: xsd:string, vendorId: xsd:long, vendorTransac
tionId: xsd:string)

print(client.service.login(log_in))
print(client.service.getStateWideLienEffectiveDate())


client.service.logout()