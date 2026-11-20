from car import Car

my_car = Car("audi", 1994)

my_car.accelerate()
my_car.accelerate()
my_car.accelerate()

print(my_car.get_speed())

my_car.brake()

print(my_car.get_speed())

print(my_car(), my_car.get_speed())
