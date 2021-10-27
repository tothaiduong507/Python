#index operator []= gives access to a sequence's element(str,list, tuples)

name= "minh do"
if (name[0].islower()) :
    name= name.capitalize()

firt_name=name[:4].upper()
last_name= name[5:7:1]
last_character= name[-1]
print(firt_name)
print(last_name)
print(last_character)