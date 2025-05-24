class Car:
    def __init__(self):
        print('this is a initialization method')
    
    def details(self):
        print('this is car detail function')
        
bmw = Car()
bmw.details()

print(type(bmw))
