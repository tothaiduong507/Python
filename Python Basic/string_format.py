#str.format()= optionnal method that gives
#users mre control when displaying output

animal="cow"
item="moon"
print("The {} jumped over the {}".format(animal,item))
#positional argument
print("The {0} jumped over the {1}".format(animal,item))
#keyword argument
print("The {name} jumped over the {object}".format(name="Cowboy",object="wall"))
text= "The {} jumped over {}"
print(text.format(animal,item))

name= "Minh"

print("Hello, my name is {:10}. Nice to meet ya".format(name))
print("Hello, my name is {:>10}. Nice to meet ya".format(name))

number = 3.14159
number2= 1000
print("The number pi is {:.2f}".format(number))

print("The number is {:,}".format(number2))
#in binary code
print("The number is {:b}".format(number2))