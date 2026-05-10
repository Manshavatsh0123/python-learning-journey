words=["Twinkle","Star" ,'poem']

with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/Read.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word ,"#" * len(words))


with open("/home/mansha-vatsh/Desktop/Pyton/python-learning-journey/Chapter9/Read.txt","w") as f:
    f.write(content)