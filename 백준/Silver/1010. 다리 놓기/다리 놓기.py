import sys

case = int(sys.stdin.readline())
answer=[]
for i in range(case):
    left, right = sys.stdin.readline().split()
    left = int(left)
    right = int(right)
    n, r = 1, 1
    for i in range(left+1, right+1):
        n= n*i
    for i in range(1, right-left+1):
        r = r*i
    answer.append(int(n/r))

for i in range(len(answer)):
    print(answer[i])
