class Car:

    top_speed = 30

    def __init__(self, make, year):

        if not isinstance(make, str):
            raise TypeError("make is not a string")
        if not isinstance(year, int):
            raise TypeError("year is not an integer")

        self.__make = make
        self.__year = year
        self.__speed = 0

#defining ways to increase and decrease speed as well as a way to call the final speed

    def accelerate(self):
        if self.__speed + 5 >= self.top_speed:
            raise TypeError("The speed is too high")
        else:
            self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
