def determine_safe(report, i, dire, bad):
    if i >= len(report):
       return True
    elif dire == -1:
        if report[i] > report[i + 1]:
            dire = 0
        else:
            dire = 1
        return determine_safe(report, i + 1, dire, bad)

    if dire == 0:
        if report[i - 1] + report[i] < report[i - 1] * 2 and abs(report[i - 1] - report[i]) <= 3:
            return determine_safe(report, i + 1, dire, bad)
        elif bad == 0:
            report.pop(i)
            return determine_safe(report, 0 if i == 1 else i, -1 if i == 1 else dire, 1)
        else:
            return False
    elif dire == 1:
        if report[i - 1] + report[i] > report[i - 1] * 2 and abs(report[i - 1] - report[i]) <= 3:
            return determine_safe(report, i + 1, dire, bad)
        elif bad == 0:
            report.pop(i)
            return determine_safe(report, 0 if i == 1 else i, -1 if i == 1 else dire, 1)
        else:
            return False

with open('Input_2.txt', 'r') as input:
    safe_levels = 0

    for line in input:
        # Convert to list
        report = list(map(int, line.split()))

        if determine_safe(report, 0, -1, 0):
            safe_levels += 1
        else:
            report.pop(0)
            if determine_safe(report, 0, -1, 1):
                safe_levels += 1


print(f"Safe levels: {safe_levels}")