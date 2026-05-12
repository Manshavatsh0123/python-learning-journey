class Employee:
    company="ITC"
    salary=9000
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

class coder:
    language="Python"
    def printlanguages(self):
        print(f"Out of all the language here is your language: {self.language}")


class Programmer(Employee,coder):
    company="ITC Infotech"
    salary=9000
    def showLanguage(self):
        print(f"The name is {self.company} and the salary is {self.salary}")


a = Employee()
b = Programmer()

b.show()
b.printlanguages()
b.showLanguage()


# The name is ITC Infotech and the salary is 9000
# Out of all the language here is your language: Python
# The name is ITC Infotech and the salary is 9000
