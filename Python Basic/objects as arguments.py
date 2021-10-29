class Car:
    color = None
class Motorcycle:
    color= None
def changecolor(vehicle,color):
    vehicle.color= color

car_1=Car()
print(car_1.color)
changecolor(car_1,"black")
print(car_1.color)

bike_1 = Motorcycle()
changecolor(bike_1,"red")
print(bike_1.color)