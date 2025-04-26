#7.1
car = input("Enter the name of car : ")
print(f"Let me see if I can find you a {car}.")



#7.2
num_people = int(input("How many people are in your group? "))

if num_people > 8:
  print("wait for a table.")
else:
  print("table is ready.")


  
#7.3
number = int(input("Enter a number: "))

if number % 10 == 0:
  print(f"The number {number} is a multiple of 10.")
else:
  print(f"The number {number} is not a multiple of 10.")


  
#7.4
while True:
  topping = input("Enter a pizza topping (or 'exit' to finish): ")
  if topping.lower() == 'exit':
    break
  else:
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza is being prepared with the toppings you selected!")



#7.5
while True:
  age_string = input("Please enter your age(or enter 'exit' for leave) : ")
  if age_string.lower() == 'exit':
      break
  age = int(age_string)
  if age < 3:
    print("Your movie ticket is free.")
  elif 3 <= age <= 12:
    print("Your movie ticket costs $10.")
  else:
    print("Your movie ticket costs $15.")

print("Thank you for your purchase!")



#7.6
toppings = []

while True:  
  topping = input("Enter a pizza topping (or 'quit' to finish): ")
  if topping.lower() == 'quit':
    break  
  else:
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza will have the following toppings:")
for topping in toppings:
  print(f"- {topping}")
print("Enjoy your pizza!")



#7.7
while True:
  print("Infinite while loop")