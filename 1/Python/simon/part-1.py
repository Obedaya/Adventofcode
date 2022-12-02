import fileinput

cal = 0
maxcal = 0

for line in fileinput.input(files='input.txt'):
    if line != '\n':
        line = line[:-1]
        cal += int(line)
        if maxcal < cal:
                maxcal = cal
    else: cal = 0
print(maxcal)