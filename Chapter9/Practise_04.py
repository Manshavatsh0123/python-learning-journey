word="Donkey"

with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/Update.txt","r") as f:
    content = f.read()

contentNew = content.replace(word ,"######")

with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/Update.txt","w") as f:
    f.write(contentNew)