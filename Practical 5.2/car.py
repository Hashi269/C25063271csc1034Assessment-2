class Car:
    def __init__(self, make, year):

        if not isinstance(make, str):
            raise TypeError("make is not a string")
        if not isinstance(year, int):
            raise TypeError("year is not an integer")

        self.make = make
        self.year = year
        self.speed = 0

#defining ways to increase and decrease speed as well as a way to call the final speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

