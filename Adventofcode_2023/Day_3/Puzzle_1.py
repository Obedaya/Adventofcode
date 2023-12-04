def is_symbol(char):
    return char not in '0123456789.'

def extract_surrounding_chars(matrix, row, col, num_length):
    # Calculate the start column of the number
    start_col = col - num_length + 1

    # Collect surrounding characters
    surrounding_chars = []

    # Above and below
    for c in range(start_col, col + 1):
        if row > 0:  # Above
            surrounding_chars.append(matrix[row - 1][c])
        if row < len(matrix) - 1:  # Below
            surrounding_chars.append(matrix[row + 1][c])

    # Left
    if start_col > 0:
        surrounding_chars.append(matrix[row][start_col - 1])

    # Right
    if col < len(matrix[row]) - 1:
        surrounding_chars.append(matrix[row][col + 1])

    return surrounding_chars

def sum_part_numbers(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        matrix = [list(line) for line in lines]

    sum_of_parts = 0
    current_number = ''
    length_of_number = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            char = matrix[row][col]
            if char.isdigit():
                current_number += char
                length_of_number += 1
                if col == len(matrix[row]) - 1 or not matrix[row][col + 1].isdigit():
                    if any(is_symbol(sym) for sym in extract_surrounding_chars(matrix, row, col, length_of_number)):
                        sum_of_parts += int(current_number)
                    current_number = ''
                    length_of_number = 0
            else:
                current_number = ''
                length_of_number = 0
    return sum_of_parts

if __name__ == '__main__':
    sum_of_parts = sum_part_numbers("Input_1.txt")
    print("Sum: ", sum_of_parts)
