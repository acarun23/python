
# for loop

fruits = ['mango', 'orange', 'apple']

for item in fruits:
    print(item, end =' ')

# for loop with range(initial_value, limit, increment_value)
print("\n\nfor loop with range output:")
for i in range(5, 15, 2):
    if i % 3 == 0:
        print(i, "\nvalue divisible by 3")
    else:
        print(i,end=' ')

# while loop
i = 0
print("\n\nwhile loop output:")
while i < 10:
    i = i+1
    if i == 2:
        continue
    elif i == 5:
        pass
    elif i == 7:
        break
    print(i,end =' ')