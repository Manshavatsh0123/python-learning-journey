import os

# Specify the directory you want to list
path = "/home/mansha-vatsh/Desktop"

# List all the file and directory in the specified path
files = os.listdir(path)

# Print each file and directory name
print("Directory contents:")
for file in files:
    print(file)