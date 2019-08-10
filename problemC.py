# Solution by Artem Bakhanov #

n = int(input())

for i in range(n):
    line = input().split()
    marks = {"A": 0, "B": 0, "C": 0, "D": 0}
    for mark in line:
        marks[mark] += 1
    answer = 36000
    if marks["C"] or marks["D"]:
        answer = 12000
    elif marks["B"] > 2:
        answer = 18000
    elif marks["B"]:
        answer = 24000
    print(answer)
