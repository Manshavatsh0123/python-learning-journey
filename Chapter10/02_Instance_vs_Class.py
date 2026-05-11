
#Class attribute
class Employee:
    language = "py" # this is class attribute
    salary=1200000


mansha = Employee()
mansha.language='Java' # this is instance attribute
print(mansha.language,mansha.salary) 
