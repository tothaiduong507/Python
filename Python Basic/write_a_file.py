text="Yoooooooo\nThis is some text \nHave a good one"
try:
    with open('F:\\TT HCM\\week1.txt','w') as file:
        file.write(text)
except FileNotFoundError:
    print("That file is not found")