import random 

def game():

    print("You are playing game.")
    score = random.randint(1, 62)

    with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/hiscore.txt", "r") as f:
        hiscore = f.read()

        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")

    if score > hiscore:
        print("New High Score!")

        with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()