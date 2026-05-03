a=int(input("Enter Age:"))

# if elif else ladder
if(a>18):
    print("You are above the age of consent")
    print("Good For You")
elif(a>0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:
    print("You are below the age of consent")

print("End of Program")



# Enter Age:0
# You are entering 0 which is not a valid age


# Enter Age:67
# You are above the age of consent
# Good For You

# Enter Age:89
# You are above the age of consent
# Good For You
# End of Program