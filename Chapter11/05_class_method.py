class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of is {cls.a}")
    
e = Employee()
e.a = 45

e.show() 

# The class attribute of is 1