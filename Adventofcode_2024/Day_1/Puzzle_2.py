# Open file
with open('Input_1.txt', 'r') as input:
    location_list_1 = []
    location_list_2 = []
    output_similarity = 0
    for line in input:
        loc1, loc2 = line.split()
        location_list_1.append(int(loc1))
        location_list_2.append(int(loc2))

    location_list_1.sort()
    location_list_2.sort()

    # Remove duplicates from left list
    location_list_1 = list(dict.fromkeys(location_list_1))

    for i in location_list_1:
        output_similarity += location_list_2.count(i) * i

    print(f"Output: {output_similarity}")