import re

with open("Input_3.txt", "r") as file:
    output = 0
    inp = file.read().replace("\n", "")
    do_mult = True
    multiplications = list(re.finditer(r"(?P<do>do\(\))|(?P<dont>don't\(\))|(?P<mul>mul\((\d?\d?\d),(\d?\d?\d)\))",inp))
    for multiplication in multiplications:
        grouptype = [name for name, value in multiplication.groupdict().items() if value is not None][0]
        match grouptype:
            case "mul":
                if do_mult:
                  output += int(multiplication.groups()[3]) * int(multiplication.groups()[4])
            case "do":
                do_mult = True
            case "dont":
                do_mult = False
            case _:
                exit(1)

print(f"Output: {output}")