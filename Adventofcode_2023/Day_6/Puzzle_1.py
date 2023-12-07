import re

def count_wins(total_time, highscore):
    win_count = 0

    for charging_time in range(1, total_time):
        traveling_time = total_time - charging_time
        distance = charging_time * traveling_time

        if distance > highscore:
            win_count += 1

    return win_count


if __name__ == '__main__':
    with open("Input_1.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    times = re.findall(r'\d+', lines[0])
    times = [int(num) for num in times]

    distances = re.findall(r'\d+', lines[1])
    distances = [int(num) for num in distances]

    amount_races = 1

    for i in range(len(times)):
        amount_races *= count_wins(times[i], distances[i])

    print(amount_races)
