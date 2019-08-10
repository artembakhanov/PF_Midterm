# Solution by Artem Bakhanov #

n, m = map(int, input().split())

votes = [0] * n
candidate = 0
for i in range(m):
    vote = int(input().split()[1]) - 1
    votes[vote] += 1
    if votes[vote] > votes[candidate]:
        candidate = vote

print(candidate + 1)