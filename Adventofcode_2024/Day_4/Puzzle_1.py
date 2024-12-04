def traverse_letters(matrix, start, end, step, letter):
    count = []
    ind = 0
    for x in range(start, end, step):
        for y in range(start, end, step):
            if matrix[x][y] == letter:
                count.insert(ind, True)
            else:
                count.insert(ind, None)
            ind += 1
    return count

def calculate_xmas(xmas_matrix):
    m_count = traverse_letters(xmas_matrix, 2, 5, 1, 'M')
    a_count = traverse_letters(xmas_matrix, 1, 6, 2, 'A')
    s_count = traverse_letters(xmas_matrix, 0, 7, 3, 'S')
    xmas_count = 0
    for i in range(9):
        if m_count[i] and a_count[i] and s_count[i]:
            xmas_count += 1
    return xmas_count

def get_xmas_matrix(matrix, row, col):
    xmas_matrix = []

    for i in range(row - 3, row + 3 + 1):
        subrow = []
        for j in range(col - 3, col + 3 + 1):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                subrow.append(matrix[i][j])
            else:
                subrow.append(None)
        xmas_matrix.append(subrow)

    return xmas_matrix

with open("Input_4.txt", "r") as file:
    # Populate matrix
    matrix = []
    output = 0
    for line in file:
        matrix.append(list(line))

    # Search for X
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                xmas_matrix = get_xmas_matrix(matrix, i, j)
                output += calculate_xmas(xmas_matrix)

print(f"Output: {output}")

