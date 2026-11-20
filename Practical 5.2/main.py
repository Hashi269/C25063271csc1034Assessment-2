from car import Car

my_car = Car("audi", 1994)

my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
#my_car.accelerate() #should raise a Type Error

print(my_car.get_speed())

my_car.brake()
my_car.brake()
my_car.brake()
my_car.brake()
#my_car.brake() #should raise a Type Error

print(my_car.get_speed())


