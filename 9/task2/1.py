lines_file = open('zen.txt', 'r', encoding='utf-8')
lines = []
for line in lines_file:
    if line != '\n':
        lines.append(line)
lines.reverse()
lines[0] = lines[0] + '\n'
for line in lines:
    print(line, end = '')