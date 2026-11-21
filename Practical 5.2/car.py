import datetime as dt

class Car:

    __top_speed = 30
    __stationary = 0

    def __init__(self, make, year, color, category):

        if year is None :
            raise ValueError("year cannot be None")
        if make is None:
            raise ValueError("make cannot be None")
        if year is None :
            raise ValueError("year cannot be None")
        if color is None :
            raise ValueError("color cannot be None")
        if category is None:
            raise ValueError("category cannot be None")

        if not isinstance(category, str):
            raise TypeError("category is not a string")
        if not isinstance(color, str):
            raise TypeError("color is not a string")
        if not isinstance(make, str):
            raise TypeError("make is not a string")
        if not isinstance(year, int):
            raise TypeError("year is not an integer")

        self.__make = make
        self.__year = year
        self.__color = color
        self.__category = category
        self.__speed = 0

#defining ways to increase and decrease speed as well as a way to call the final speed

    def accelerate(self):
        if self.__speed + 5 >= self.__top_speed:
            raise TypeError("The speed is too high")
        else:
            self.__speed += 5

    def brake(self):
        if self.__speed - 5 <= self.__stationary:
            raise TypeError("The car is already fully braked")
        else:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed

              #-----defining ways to access the cars attributes as well as setting new ones-----

# way to set and get the make of the car

    def set_make(self, new_make):
        self.__make = new_make

    def get_make(self):
        return self.__make

#way to set and get the year of the car

    def set_year(self, new_year):
        self.__year = new_year

    def get_year(self):
        return self.__year

# way to set and get the color of the car

    def set_color(self, new_color):
        self.__color = new_color

    def get_color(self):
        return self.__color

# way to set and get the category of the car

    def set_category(self, new_category):
        self.__category = new_category

    def get_category(self):
        return self.__category

    def age(self):
        current_year = dt.date.today().year
        return current_year - self.__year


# way to lay out all the cars attributes

    def __str__(self):
        return "make={}, year={}, color={}, category={}".format(self.__make, self.__year, self.__color, self.__category)


