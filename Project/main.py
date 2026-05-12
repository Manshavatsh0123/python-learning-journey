import random

n=random.randint(1,100)

a=-1
gusses=0

while (a != n):
    a=int(input("Guess the number: "))

    if(a>n):
        print("Lower number please.")
        gusses+=1
    elif(a<n):
        print("Higher number please.")
        gusses+=1
    

print(f"You have gusses the number {n} correctly in {gusses} attempt")


# Guess the number: 56
# Lower number please.
# Guess the number: 45
# Lower number please.
# Guess the number: 34
# Lower number please.
# Guess the number: 22
# Lower number please.
# Guess the number: 12
# Lower number please.
# Guess the number: 10
# Lower number please.
# Guess the number: 2
# Higher number please.
# Guess the number: 3
# Higher number please.
# Guess the number: 6
# Lower number please.
# Guess the number: 5
# Higher number please.
# You have gusses the number 5 correctly in 10 attempt
