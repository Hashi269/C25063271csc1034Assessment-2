from car import Car

class CarManager:
    def init_car(self,path):
        self.__cars = []
        with open(path,"r") as file:
            for line in file:
                params = line.strip().split(",")
                self.__cars.append(Car(params[0], params[1], params[2], params[3]))

    def get_cars(self):
        return self.__cars