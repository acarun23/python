
line_to_modify = 2
new_text = "added at line 2\n"
with open('write_data.txt', '+r') as file:
    lines = file.readlines()
    # lines index will start from 0
    if line_to_modify-1 < len(lines):
        lines[line_to_modify-1] = new_text


with open('write_data.txt', '+r') as file:
    file.writelines(lines)
    file.writelines("new line at the end\n")