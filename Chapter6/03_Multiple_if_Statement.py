a=int(input("Enter Age:"))

# If Statement Number 1
if(a%2 == 0):
    print("a is even")

# If Statement Number 2
if(a>18):
    print("You are above the age of consent")
    print("Good For You")
elif(a>0):
    print("You are entering an invalid negative age")
else:
    print("You are below the age of consent")

print("End of Program")