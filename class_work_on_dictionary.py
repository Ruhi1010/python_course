# 6-4
glossary = {
     'dictionary': 'It is basically Hash-map',
     'list': 'It is basically an array.',
     'tuple': 'An immutable list.'
}
for key,val in glossary.items():
    print(f"key:{key}")
    print(f"value:{val}") 
print()
print()

# 6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'padma': 'bangladesh'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"{river.title()}")

print()

for country in rivers.values():
    print(f"{country.title()}")


# 6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'sarah', 'ruhi', 'rishat', 'edward', 'phil', 'rakib']
for person in people:
    if person in favorite_languages:
        print(f"Thank you {person.title()}, for the pole")
    else:
        print(f"Not Thanking you {person.title()}")
