def hello(**kwargs) :
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(last="Minh",first="Do",middle="Tuan")


