#7.4
while True:
  topping = input("Enter a pizza topping (or 'exit' to finish): ")
  if topping.lower() == 'exit':
    break
  else:
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza is being prepared with the toppings you selected!")



