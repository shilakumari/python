class Patient:

    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.clinical=[]

    def addClinicalData(self,clinical):
        self.clinical.append(clinical)

class Clinical:
    def __init__(self,componentName,componentValue):
        self.componentName=componentName
        self.componentValue=componentValue

p1=Patient("Xyz",89)
c1=Clinical("bp","80/120")
p1.addClinicalData(c1)
c2=Clinical("heart rate","80")
p1.addClinicalData(c2)
for eachClinical in p1.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)
