import random

x= random.randint(0,10)
#random between 0 and 1
y= random.random()
print(x)
print(y)

myList=['rock','paper','scissors']
z= random.choice(myList)
print(z)

cards=[1,2,3,4,5,6,7,8,9,"J","Q","K"]
random.shuffle(cards)

print(cards)