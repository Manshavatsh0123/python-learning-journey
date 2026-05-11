class Programmer:
    company="Micrsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p=Programmer("Harry",1200000,851101)
print(p.name,p.salary,p.pin,p.company) # Harry 1200000 851101 Micrsoft

r=Programmer("Rohan",1200000,851101)
print(r.name,r.salary,r.pin,r.company) # Rohan 1200000 851101 Micrsoft
       