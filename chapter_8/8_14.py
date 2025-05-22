#8.14
def make_car(manufacturer, model, **options):
        options['manufactured_by']= manufacturer
        options['model']= model
        return options

car = make_car('subaru', 'outback', 
               color='blue', 
               tow_package=True)

print(car)
