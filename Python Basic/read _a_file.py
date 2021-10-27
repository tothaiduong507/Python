try:
    with open('F:\\TT HCM\\week1.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found")
#print(file.closed)