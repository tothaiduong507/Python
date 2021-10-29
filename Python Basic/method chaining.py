class Car:
    def turn_on(self):
        print("You turn on the car")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You stop on the car")
        return self
    def turn_off(self):
        print("You turn off the car")
        return self
car= Car()
car.turn_on().drive()