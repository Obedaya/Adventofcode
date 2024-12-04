import re

with open("Input_3.txt", "r") as file:
    output = 0
    for line in file:
        multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        for multiplication in multiplications:
            result = 1
            for number in multiplication:
                result *= int(number)
            output += result

print(f"Output: {output}")