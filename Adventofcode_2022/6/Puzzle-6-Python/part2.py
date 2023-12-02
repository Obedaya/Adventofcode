file = open("input6.txt").readline().strip()
for i in range(len(file)):
    if len(set(file[i:i+14])) == 14:
        exit(print(i + 14))