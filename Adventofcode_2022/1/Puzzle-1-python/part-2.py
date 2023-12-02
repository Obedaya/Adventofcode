import fileinput

cal = 0
maxcal = [0, 0, 0]
index = 0
top = len(maxcal)

def shift(i):
    if i < top:
        for j in range(top-1):
            if j > i:
                maxcal[j] = maxcal[j-1]
                j-1

def setmaxcal(tmpcal, i):
    if i >= top: return
    if tmpcal > maxcal[i]:
        shift(i)
        maxcal[i] = tmpcal
    else:
        setmaxcal(tmpcal, i+1)

for line in fileinput.input(files='input.txt'):
    if line != '\n':
        line = line[:-1]
        cal += int(line)
        setmaxcal(cal, 0)

    else:
        print("Index:", index, "Cal:", cal)
        cal = 0
        index += 1

print(maxcal)
print(sum(maxcal))