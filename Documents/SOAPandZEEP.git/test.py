import zeep

wsdl = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
a = client.service.CelsiusToFahrenheit("100")
