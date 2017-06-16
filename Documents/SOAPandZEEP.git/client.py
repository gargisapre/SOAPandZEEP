import zeep

"""
Here we set up the client and the wsdl file
"""
client = zeep.Client(wsdl=wsdl)
"""
this block gives youi the information to login 
"""
login_info = client.get_type('ns0:loginInfo')
log_in = login_info(firmId=, loginId='', password='')

"""
Here you have the information for a test childsupport search
the first block of code defines a name for the search 
the middle chunk creates a namelist which is one of the parameters for the child support order. it does this by creating an array containing the name we just created
the third block creates the order using the documentation on the pdf
"""
child_support_name = client.get_type('ns0:childSupportName')
csName = child_support_name(searchExactName='False', firstName="KAREN", lastName="KANE", fromDate='01/03/1997', toDate='03/04/1997')

nameList = [csName]

child_Support_Order= client.get_type('ns0:childSupportOrder')
csOrder = child_Support_Order(deliveryMethod='Email', deliveryInfo='gargisapre@gmail.com', reference = 'test', vendorId=99, clientFirmNumber='9999', name=nameList )


# state_Wide_Lien_Order = client.get_type('ns0:stateWideLienOrder')
# sWLO = state_Wide_Lien_Order(deliveryMethod='Web', reference='Gargi', vendorId=9999)

"""
Here you have the information for the patriot search
the first block of code defines a name for the search
the middle chunk creates a namelist which is one of the parameteres for the patriot search order. it does this by creating an array containing the name we just created
the third block creaetes the order using the documentation on the pdf
"""
patriot_name = client.get_type('ns0:patriotName')
pName = patriot_name(searchExactName='False',firstName='KAREN',lastName='KANE',fromDate='01/03/1997',toDate='03/04/1997')

nameList2=[pName]

patriot_order = client.get_type('ns0:patriotOrder')
pOrder = patriot_order(deliveryMethod='Email', deliveryInfo='gargisapre@gmail.com', reference = 'test', vendorId=99, clientFirmNumber='9999', name=nameList2)

"""
Here you have information to for the wetland order
All you do is create the wetland order using the documentation. You can define the specific properties such as the address and the
county using pre approved addresses
"""
wetland_order = client.get_type('ns0:wetlandOrder')
wOrder = wetland_order(vendorId=99,address='139 BROADWAY', county='MONMOUTH',owner = 'GILBERT GRIEDER',deliveryMethod='Email',deliveryInfo='gargisapre@gmail.com', municipality='FREEHOLD', municipalityType='T', reference='wtest', state='NJ')


"""
Here you have the information for the flood order
All you do is create the wetland order using the documentation. You can define the specific properties such as the address and the
county using pre approved addresses 
"""
flood_order = client.get_type('ns0:floodOrder')
fOrder = flood_order(address='139 BROADWAY', county='MONMOUTH', deliveryInfo='gargisapre@gmail', deliveryMethod='Email',municipality='FREEHOLD', municipalityType='T', propertyDesignation1='19', propertyDesignation2='57',  reference='ftest', state='NJ', vendorId=99)


"""
Down here is where you run each method and print the results which should give you an XML confirmation for the order(s) you just placed
"""

"""
first you log in and validate your 
"""
print(client.service.login(log_in)) 
a = client.service.validate('test', 0)
print(a)

"""
this is running and printing the results of the child support order
"""
# print(client.service.submitChildSupport(csOrder))
"""
this is running and printing the results of the statewidelien effective date
"""
# print(client.service.getStateWideLienEffectiveDate())
"""
this is running and printing the results of the patriot order
"""
# print(client.service.submitPatriot(pOrder))
"""
this is running and printing the results of the statewide lien 
"""
# print(client.service.submitStateWideLien(sWLO))
"""
this is running and printing the results of the wetland order
"""
# print(client.service.submitWetland(wOrder))
"""
this is running and printing the results of the submit flood order
"""
print(client.service.submitFlood(fOrder))
"""
this is logging you out of the system
"""
client.service.logout()
