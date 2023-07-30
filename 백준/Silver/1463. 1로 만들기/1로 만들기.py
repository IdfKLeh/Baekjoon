import sys

x = int(sys.stdin.readline())
answer=[10000000000]*(x*3+1)
answer[1]=0
for i in range(1,x+1):
    if answer[i+1]>(answer[i]+1):
        answer[i+1]=answer[i]+1
    if answer[i*2]>(answer[i]+1):
        answer[i*2]=answer[i]+1
    if answer[i*3]>(answer[i]+1):
        answer[i*3]=answer[i]+1


print(answer[x])