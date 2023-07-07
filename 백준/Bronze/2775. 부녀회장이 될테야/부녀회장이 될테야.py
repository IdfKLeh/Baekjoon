import sys

test = int(sys.stdin.readline())
target=[[0 for i in range(2)] for i in range(test)]
floor = 0
num = 0
for i in range(test):
    target[i][0] = int(sys.stdin.readline())
    target[i][1] = int(sys.stdin.readline())
    if target[i][0] >= floor:
        floor = target[i][0]+1
    if target[i][1] >= num:
        num = target[i][1]+1
apart = [[i for i in range(num)] for i in range(floor)]
for i in range(1,floor):
    for j in range(1,num):
        apart[i][j] = apart[i-1][j]+apart[i][j-1]
for i in range(test):
    print(apart[target[i][0]][target[i][1]])

