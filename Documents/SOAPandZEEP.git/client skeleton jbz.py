import zeep
import openpyxl

select = 2   #0 = alalnsis, 1 = dev, 2 = test
method = ['alalnsis', 'dev', 'test']
endpoint = ['http://alalnsis008.risk.regn.net:8080/ws/signon?wsdl',
            'http://sis-jas-dev.risk.regn.net:8080/ws/signon?wsdl',
            'http://sis-jas-test.risk.regn.net:8080/ws/signon?wsdl']
print('Using ' + method[select] + ' as endpoint')
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
wetOrder  = client.get_type('ns0:wetlandOrder')
floodOrder= client.get_type('ns0:floodOrder')
CGSOrder  = client.get_type('ns0:certificateOfGoodStanding')
statusOrder  = client.get_type('ns0:corporateStatusOrder')
certUCCOrder = client.get_type('ns0:stateCertifiedUccOrder')
UCCOrder  = client.get_type('ns0:uccOrder')
franchiseOrder    = client.get_type('ns0:franchiseTaxOrder')

client.service.login(log_in)
#client.service.logout()    #test statefulness by logging in prematurely

ref = ['A_PYTHON', 'D_PYTHON', 'T_PYTHON'] #references refer to the endpoint used

i = 99  #1-97 are 'THIRD PARTY', 98 is 'SIS', 99 is 'SIGN ON'
test_CSO =  childSupportOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                          reference=ref[select]+'_Child', vendorId=i, name=nameList )

test_Patriot =   patriotOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                          reference=ref[select]+'_Patriot',  vendorId=i, name=nameList )

test_SWLO =         lienOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com', 
	                          reference=ref[select]+'_Lien',  vendorId=i, name=nameList )

test_TLO =          tideOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_Tide', vendorId=i, county='ATLANTIC',
	                          block=37, lot=3, municipality='ABSECON', municipalityType='CITY',
	                          address='1006 NEW YORK AVE', state='NJ', mapRequestId=1,
	                          hasGrantPackagePricing=True, isGrantRequested=True)

test_WLO =           wetOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_Wet', vendorId=i, county='MERCER',
	                          address="3 FINDLEY LANE", municipality='WEST WINDSOR', municipalityType='TOWNSHIP',
	                          owner='FANG SHU', state='NJ')

test_Flood =       floodOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
  	                          reference=ref[select]+'_Flood', vendorId=i, county='ATLANTIC',
 	                          address='1835 EMERSON AVE', municipality='ATLANTIC', municipalityType='CITY', state='NJ')

test_CGS =           CGSOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_Certificate', vendorId=i, stateSelection="NJ",
	                          businessName='ABC Inc', entityType='LLC', goodStandingCertTypeId='5' )

test_status =     statusOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_Status', vendorId=i, stateSelection="NJ",
	                          businessName='ABC Inc', entityType='LLC', hasPackagePricing=False )

test_certUCC =   certUCCOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_CertGCC', vendorId=i, copyOfLiens=1,
	                          state='NJ', businessName='ABC Inc')

test_UCC =           UCCOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_GCC', vendorId=i, copyOfLiens=1,
	                          forThisAddressOnly=True, businessName='ABC Inc', county='Mercer')

test_franchise=franchiseOrder(deliveryMethod='email', deliveryInfo='JZhang@signatureinfo.com',
	                          reference=ref[select]+'_Franchise', vendorId=i, stateOfIncorporation='NJ',
	                          businessName='ABC Inc', entityType='LCC', hasPackagePricing=False,
	                          transactionType='OTHER')


#print('testing getStateWideLienEffectiveDate')
#print(client.service.getStateWideLienEffectiveDate())

#print('testing getPatriotEffectiveDate')
#print(client.service.getPatriotEffectiveDate())

#print('testing submitPatriot')
#print(client.service.submitPatriot(test_Patriot))

#print('testing submitChildSupport')
#print(client.service.submitChildSupport(test_CSO))

#print('testing submitStateWideLien')
#print(client.service.submitStateWideLien(test_SWLO))

#print('testing submitTideland')
#print(client.service.submitTideland(test_TLO))

#print('testing submitWetland')
#print(client.service.submitWetland(test_WLO))

#print('testing submitFlood')
#print(client.service.submitFlood(test_Flood))

#print('testing submitCertificatOfGoodStanding')
#print(client.service.submitCertificateOfGoodStanding(test_CGS))

#print('testing submitStateCertifiedUCC')
#print(client.service.submitStateCertifiedUcc(test_certUCC))

#print('testing submitUcc')
#print(client.service.submitUcc(test_UCC))

print('testingsubmitFranchiseTaxOrder')
print(client.service.submitFranchiseTax(test_franchise))

#print('testing submitCorporateStatus')
#print(client.service.submitCorporateStatus(test_status))

#print('testing getInvoiceInformation')
#print(client.service.getInvoiceInformation(['TD-166-1003', 'CJ-165-1012']))

client.service.logout()

#NOTES
#because right now CSNames are interchangable for both PatriotNames and SWLNames
 #thus test_CSO is interchangable for both test_Patriot and test_SWLO
#submitWetland needs the parameter hasGrantPackagePricing DESPITE NOT SHOWN IN DOCUMENTATION!
#mapRequestId=2 for instant feedback, otherwise needs processing
#clientFirmNumber is in the wrong place of the documentation for SWLO
#all parameters in documentation have first char capitalized when it should be lower case
#Wetland order has no short circuit request
#Tideland and flood have short circuit requests, but must use block lot address (not name) 
#"submitCGS()" incorrect in documentation
#submitUCC NEEDS forTHisAddressOnly, contrary to documentation
#documentation for submitFranchiseTax has "submitFranchiseTaxOrder" on bottom which is outdated