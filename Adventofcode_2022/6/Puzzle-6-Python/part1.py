file = open("input6.txt").readline().strip()
for i in range(len(file)):
    if len(set(file[i:i+4])) == 4:
        exit(print(i + 4))