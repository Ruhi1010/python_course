for x in range(5,50+1,5):
    print(x)

print('--------------------------------')

arr = []
arr = list (range (0,101,2))
for i in arr:
    print(i)
print('\n')

print (max(arr))
print(min(arr))

# comprehension in python array = [value for value in range(first value , last value , jump value)]
arr = [i for i in range(1,100) if i%2==0]
print(arr) 

#slicing
arr2 = [1,2,3,4,5,6]
arr3 = arr2[2:6:2] # slicing structure: listName[first value: second value: jump value]
