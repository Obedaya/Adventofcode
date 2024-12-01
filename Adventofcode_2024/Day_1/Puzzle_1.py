# Open file
with open('Input_1.txt', 'r') as input:
    location_list_1 = []
    location_list_2 = []
    output_distance = 0
    for line in input:
        loc1, loc2 = line.split()
        location_list_1.append(int(loc1))
        location_list_2.append(int(loc2))

    location_list_1.sort()
    location_list_2.sort()

    for i in range(0, len(location_list_1)):
        output_distance += abs(location_list_1[i] - location_list_2[i])

    print(f"Output: {output_distance}")