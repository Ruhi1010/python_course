#8.1
def display_massage():
    print("From this chapter we learn about function/method of python")
display_massage()



#8.2
def favorite_book(title):
    print(f"One of my favorite book is {title.title()}")
favorite_book('Sharlok Homes')



#8.3
def make_shirt(size, massage):
    print(f"Size is: {size} and The massage print on the shirt is: {massage}")
make_shirt('XXXL', 'Last Minute Engineer')



#8.4
def make_shirts(size, massage = 'I love Python'):
    print(f"Size: {size} Massage: {massage}")
make_shirts('L')
make_shirts('M')
make_shirts('XL', "I don't believe in love")



#8.5
def describe_city(city, country = 'Bangladesh'):
    print(f"{city} is located in {country}")
describe_city('Dhaka')
describe_city('Chottogram')
describe_city('London', 'UK')