# class Car:
#     def __init__(self):
#         print('this is a initialization method')
    
#     def details(self):
#         print('this is car detail function')
        
# bmw = Car()
# bmw.details()

# print(type(bmw))



class Car:
    def __init__(self,name,model,year):
        self.name = name 
        self.model = model
        self.year = year
        self.__odometer = 0
    
    def description(self):
        print(f'car name: {self.name}')
        print('car model name: {}'.format(self.model))
        print('car release year: {}'.format(self.year))
    
    def print_odometer(self):
        print(f'the car has run {self.__odometer} kilos')
    
    def update_odometer(self,milage):
        self.__odometer += milage
        

class Bike(Car):
    def __init__(self, name , model, year):
        super().__init__(name,model,year)

audi = Car("AUDI", "A4", 2020)
audi.description()
audi.__odometer = 35
audi.print_odometer()
audi.update_odometer(20)
audi.print_odometer() 

harley = Bike('Harley', 'SportsBike', 2019)
harley.description()

class Truck(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
    
    def description(self):
        print(f'Truck Name: {self.name}')
        print(f'Truck Model: {self.model}')
        print(f'Truck Year: {self.year}')
 
ford = Truck("Ford", "F-150", 2021)
ford.description()
ford.update_odometer(100)
ford.print_odometer()
