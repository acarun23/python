keyword = 'last'

with open("data.txt",'r') as input, open("output.txt", 'w') as out:
    for line in input:
        if keyword in line:
            out.write(line)
            