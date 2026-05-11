
#Class attribute
class Employee:
    language = "py" # this is class attribute
    salary=1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    @staticmethod #Static method
    def greet():
        print("Good Morning")


mansha = Employee()
mansha.language='Java' # this is instance attribute
print(mansha.language,mansha.salary) 

mansha.getInfo()


# Java 1200000
# The language is Java.The salary is 1200000
# Good Morning