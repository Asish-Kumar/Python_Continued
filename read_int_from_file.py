file_name = input('Enter the full file name: ')
with open(file_name, 'r+') as file:
    read_lines = file.readlines()
    # remove /n character from end of each line
    lines = []
    for line in read_lines:
        line = line.strip()

        # print(line)
        lines.extend([int(x) for x in line.split(" ")])

print(lines)