import sys

prices = [0 for i in range(5)]
set = 0
least = 2000
for i in range(5):
    prices[i] = int(sys.stdin.readline())
for i in range(3):
    if prices[i]<least:
        least = prices[i]
set += least
least = 2000
for i in range(3,5):
    if prices[i]<least:
        least = prices[i]
set+=least-50
print(set)