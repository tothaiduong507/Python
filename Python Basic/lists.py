food=["pizza","hamburger","hot dog","spaghetti"]
food[0]="sushi"
#food.append("ice cream")
#food.remove("ice cream")
#food.pop()
#food.sort()
#food.clear()
#food.insert(0,"cake")
print("Menu: ")
for i in range(len(food)):
    print(str(i+1)+". "+str(food[i]))

for x in food:
    print(x)

