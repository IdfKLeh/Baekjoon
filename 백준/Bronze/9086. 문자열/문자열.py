import sys
T = int(input())
tests = [sys.stdin.readline()for i in range(T)]
for i in range(T):
    print(tests[i][0]+tests[i][-2])
    