import os

for i in range(1, 25):
    if not os.path.exists(f"Day_{i}"):
        os.makedirs(f"Day_{i}")
    if not os.path.exists(f"Day_{i}/Input_{i}.txt"):
        with open(f"Day_{i}/Input_{i}.txt", "w") as file:
            file.write("")
    if not os.path.exists(f"Day_{i}/Puzzle_1.py"):
        with open(f"Day_{i}/Puzzle_1.py", "w") as file:
            file.write("")
    if not os.path.exists(f"Day_{i}/Puzzle_2.py"):
        with open(f"Day_{i}/Puzzle_2.py", "w") as file:
            file.write("")