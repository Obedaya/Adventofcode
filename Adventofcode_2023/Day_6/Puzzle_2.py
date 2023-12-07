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

    time = re.findall(r'\d+', lines[0])
    time = int("".join(time))

    distance = re.findall(r'\d+', lines[1])
    distance = int("".join(distance))

    amount_races = 1

    amount_races *= count_wins(time, distance)

    print(amount_races)
