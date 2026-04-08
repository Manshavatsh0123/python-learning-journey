s={1,25,5,2,2,2,35,"Harry"}

print(s,type(s)) # {1, 2, 35, 5, 'Harry', 25} <class 'set'>

s.add(344)
print(s,type(s)) # {1, 2, 35, 'Harry', 5, 344, 25} <class 'set'>

s.remove(25)
print(s,type(s)) # {1, 2, 35, 5, 344, 'Harry'} <class 'set'>