#problem 4.3
for var1 in range(1,21):
    print(var1)
    
#problem 4.4
number = list(range(1,1000001))

for var2 in number:
   print(var2)
    
#problem 4.5
print(max(number))
print(min(number))
print(sum(number))

#problem 4.6
for var3 in range(1,20,2):
    print(var3)

#problem 4.7
arr = list(range(3,31,3))
for var4 in arr:
    print(var4)

#problem 4.8
cubes = []
for number in range(1, 11):
    x = number**3
    cubes.append(x)

for var5 in cubes:
    print(var5)

#problem 4.9
cube = [number**3 for number in range(1, 11)]
print(cube)