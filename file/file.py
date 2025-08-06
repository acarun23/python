#import os

#print(os.curdir)
f = open("data.txt", "r")
print(f.readline())
f.close()

file = "data.txt"
with open(file) as data:
    print(data.read())

