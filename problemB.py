# Solution by Alecsey Murashko #

c1 = float(input())
s1 = float(input())
c2 = float(input())
s2 = float(input())

customer_diff = c2 - c1
seller_diff = s1 - s2

while (s2 > c2):
    c2 += customer_diff
    if (s2 - seller_diff > c2):
        s2 -= seller_diff
    else:
        s2 = c2

print(s2)