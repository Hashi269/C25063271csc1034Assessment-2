from car import Car

car1 = Car("audi", 1994, "yellow", "SUV")

car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
#car1.accelerate() #should raise a Type Error

print(car1.get_speed())

car1.brake()
car1.brake()
car1.brake()
car1.brake()
#car1.brake() #should raise a Type Error

print(car1.get_speed())

#print(car1.get_make())
#print(car1.get_year())
#print(car1.age())

print(car1)


