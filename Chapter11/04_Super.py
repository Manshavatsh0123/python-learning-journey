class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b =2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=5

# O=Employee()
# print(O.a)

# M=Programmer()
# print(M.a,M.b)

N=Manager()
print(N.a,N.b,N.c)
