import os

print(os.getcwd())

f = open("data.txt", "r")
content = f.readlines()
print(content[2])
## now index is at the end of line either close the file or use f.seek(0)
f.close()


# another way
specified_lines = [1, 3]
f = open("data.txt", "r")
for line, l_num in enumerate(f):
    if line in specified_lines:
        print(l_num)

f.close()