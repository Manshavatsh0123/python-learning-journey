with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/poem.txt", "r") as f:
    data = f.read()
    if("twinkle" in data):
        print("Twinkle is present in the content!")
    else:
        print("Not Twinkle is present in the content!")

    print(data)



# Twinkle is present in the content!

# twinkle twinkle little star 
# how I wander how you are