class Employee:
    a=1

class Programmer(Employee):
    b =2

class Manager(Programmer):
    c=3

O=Employee()
print(O.a)

M=Programmer()
print(M.a,M.b)

N=Manager()
print(N.a,N.b,N.c)
