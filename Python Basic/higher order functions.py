#accepts a function as an argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()
def hello(func):
    text= func("hello")
    print(text)

hello(loud)
hello(quiet)

#returns a function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide=divisor(5)
print(divide(4))