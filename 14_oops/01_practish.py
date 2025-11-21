class HP:
    property1="good build quality"
    property2="it is manufactured in mumbai"

    def __init__(self,ram,display,storage,processer):
        self.RAM=ram
        self.DISPLAY=display
        self.STORAGE=storage
        self.PROCESSER=processer

    def displayobj(self):
        return self.RAM,self.DISPLAY,self.STORAGE,self.PROCESSER
    
    def change_ram(self,new_ram):
        self.RAM=new_ram
    
    @classmethod
    def displaycls(cls):
        return cls.property1,cls.property2
    
    @classmethod
    def change_property2(cls,new_property):
        cls.property2=new_property

Elitebook=HP("12gb","15 inches","256","i9 13gen")
Victus=HP("12gb","17 inches","256","i7 8gen")


print(Elitebook.displayobj())
Elitebook.change_ram("16gb")
print(f"after the change:{Elitebook.displayobj()}")
print(Victus.displayobj())

print(HP.displaycls())
HP.change_property2("very bad quality")
print(f"after the change: {HP.displaycls()}")

# print(f"Elitebook: {Elitebook.RAM,Elitebook.DISPLAY,Elitebook.STORAGE,Elitebook.PROCESSER}")
# print(f"Victus: {Victus.RAM,Victus.DISPLAY,Victus.STORAGE,Victus.PROCESSER}")





#accessing using class name
# print(f"accessing using class name: {HP.property1}")
# print(f"accessing using class name: {HP.property2}")

# #accessing using objectname
# print(f"accessing using objectname: {Elitebook.property1}")
# print(f"accessing using objectname: {Elitebook.property2}")
# print(f"accessing using objectname: {Victus.property1}")
# print(f"accessing using objectname: {Victus.property2}")

