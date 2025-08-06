

# Python
- [Python](#python)
  - [Variable declaration and arithmatic operation](#variable-declaration-and-arithmatic-operation)
    - [Example](#example)
    - [Output](#output)
  - [List](#list)
    - [creating list](#creating-list)
    - [accessing list](#accessing-list)
    - [Example](#example-1)
    - [Output](#output-1)


---
## Variable declaration and arithmatic operation
[variable_operator.py](variable_operator.py)
1. variable_a = "test code"
2. variable_b = 10
3. variable_c = 2.34
4. name, age = "Arun", 20
5. access variable :- value = text[3:5] Here index 3 and 4 will be access 5 will be skipped
### Example
<pre> python
"# Variable declation"
variable_a = "test code"
variable_b = 10
variable_c = 2.34
text = "abc1234"
name, age = "Arun", 20

"# Variable access and print"
print("1. " + variable_a)
print(variable_b + variable_c)
print("2.a. %s is %d years old" % ("Rohit", 50))
print(f"2.b. {name} is {age} years old")

"# Arithmatic Operation"
text_addition = variable_a + text
print("3. " + text_addition)

"# access variable starting from index 3 and terminated to index 4. index 5 will not be taken"
value = text[3:5]
print("4. value = " + value )
print("5. " + str(int(value,base = 0)/2))
</pre>
### Output
<pre>
1. test code
12.34
2.a. Rohit is 50 years old
2.b. Arun is 20 years old 
3. test codeabc1234       
4. value = 12
5. 6.0
</pre>

## List
- set of ordered items
- have an index
- know the order
### creating list
### accessing list
### Example
<pre>
</pre>
### Output
