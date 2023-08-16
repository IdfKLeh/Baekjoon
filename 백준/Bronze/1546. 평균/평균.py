import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))

stand = max(scores)

for i in range(N):
    scores[i]= scores[i]/stand*100

print(sum(scores)/len(scores))