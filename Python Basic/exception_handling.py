try:
    numerator= int(input("Enter a number to divide: "))
    denominator= int(input("Enter a number to divide by:"))
    result =numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can not divide by 0")
except ValueError as e:
    print(e)
    #print("Something went wrong :(")
    print("You have enter a wrong value")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else :
    print(result)
finally:
    print("This will always executed")