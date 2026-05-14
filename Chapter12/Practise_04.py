try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")


# Enter a : 5
# Enter b : 0
# Infinite