a = int(input("Enter number input by users 1:"))
b = int(input("Enter number input by users 2:"))
c = int(input("Enter number input by users 3:"))
d = int(input("Enter number input by users 4:"))

if(a>b and a>c and a>d):
    print("Greatest Number is a")
elif(b>a and b>c and b>d):
    print("Greater Number is b")
elif(c>a and c>b and c>d):
    print("Greater Number is c")
else:
    print("Greter Number is d")

