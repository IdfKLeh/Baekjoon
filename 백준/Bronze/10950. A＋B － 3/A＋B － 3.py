import sys
tests = int(sys.stdin.readline())
answers =[0]*tests
for i in range(tests):
    a, b = map(int,sys.stdin.readline().split())
    answers[i] = a+b

for i in range(tests):
    print(answers[i])
    