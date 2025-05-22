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



