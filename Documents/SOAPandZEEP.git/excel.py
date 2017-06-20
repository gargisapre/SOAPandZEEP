import ezodf
from ezodf import newdoc, Sheet, Heading
"""
Writing a sheet
"""
# ods = newdoc(doctype='ods', filename='fun.ods')
# sheet = Sheet('SHEET', size=(10, 10))
# ods.sheets += sheet
# sheet['A1'].set_value("cell with text")
# sheet['B2'].set_value(3.141592)
# sheet['C3'].set_value(100, currency='USD')
# sheet['D4'].formula = "of:=SUM([.B2];[.C3])"
# pi = sheet[1, 1].value
# print(sheet['A1'].value)

"""
Reading from a sheet
"""
doc = ezodf.opendoc('fun.ods')
sheet = doc.sheets[0]

print(sheet['A1'].value)
"""
BE SURE TO SAVE!!!
"""
doc.save()
