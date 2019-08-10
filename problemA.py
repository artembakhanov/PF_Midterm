# Solution by Artem Bakhanov #

secs = int(input())
day = secs % 60 * 60 * 24 * 30 // (60 * 60 * 24) + 1
month = secs % 31104000 // (30 * 24 * 60 * 60) + 1
year = 1970 + secs // 31104000 # 31104000 = 60 * 60 * 24 * 30 * 12
print(f"{day:02d}.{month:02d}.{year}")
