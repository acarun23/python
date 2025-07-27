fruits = ["apple", "orange", "banana"]
print("1.", end=" ")
print(fruits)

# access element
print("2.", end=" ")
print(fruits[1])
print("3.", end=" ")
print(fruits[1:3])      # slicing doesn't conssider last element

# addition/ deletion
fruits.append("mango")
del fruits[1]       # delete element at 1st index i.e. organge
fruits[0] = "cherry" # modify element at 0th index i.e. apple
total = len(fruits) # get length of list
print(f"4. total element {total}, names {fruits}")

