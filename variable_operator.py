# Variable declation
variable_a = "test code"
variable_b = 10
variable_c = 2.34
text = "abc1234"
name, age = "Arun", 20

# Variable access and print
print("1. " + variable_a)
print(variable_b + variable_c)
print("2.a. %s is %d years old" % ("Rohit", 50))
print(f"2.b. {name} is {age} years old")

# Arithmatic Operation
text_addition = variable_a + text
print("3. " + text_addition)

# access variable starting from index 3 and terminated to index 4. index 5 will not be taken
value = text[3:5]
print("4. value = " + value )
print("5. " + str(int(value,base = 0)/2))

