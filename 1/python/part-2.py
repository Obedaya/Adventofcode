import fileinput

cal = 0
maxcal = [0, 0, 0]
index = 0
top = len(maxcal)

#def setmaxcal(tmpcal):
#    if maxcal[top-1] < tmpcal:
#        if maxcal[top-2] < tmpcal:
#            if maxcal[top-3] < tmpcal:
#                maxcal[top-2] = maxcal[top-3]
#                maxcal[top-1] = maxcal[top-2]
#                maxcal[top-3] = tmpcal
#            else:
#                maxcal[top-1] = maxcal[top-2]
#                maxcal[top-2] = tmpcal
#        else:
#            maxcal[top-1] = tmpcal
#def setmaxcal(tmpcal, i):
#    if i < 3 and tmpcal >= maxcal[i]:
#        if i == 2:
#            maxcal[i] = tmpcal
#        setmaxcal(tmpcal, i + 1)
#    elif i > 0 and i < 3:
#            maxcal[i-1] = maxcal[i]
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