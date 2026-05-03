mark1 = int(input("Enter number input by marks 1:"))
mark2 = int(input("Enter number input by marks 2:"))
mark3 = int(input("Enter number input by marks 3:"))

total_percentage =(100*(mark1 + mark2 + mark3)) /300

if(total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >=33):
    print("You are pass:",total_percentage)
else:
    print("You are fail",total_percentage)


# Enter number input by marks 1:45
# Enter number input by marks 2:56
# Enter number input by marks 3:89
# You are pass: 63.333333333333336