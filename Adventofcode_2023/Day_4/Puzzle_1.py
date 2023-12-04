if __name__ == '__main__':
    f = open("Input_1.txt", 'r')
    lines = f.readlines()

    sum_totals = 0

    for line in lines:
        total = 0
        line = line.split("|")
        winning_numbers = line[0].lstrip(":").split()
        numbers = line[1].split()

        for i in winning_numbers:
            if i in numbers and total != 0:
                total *= 2
            elif i in numbers:
                total = 1

        sum_totals += total

    print("Sum of numbers: ", sum_totals)