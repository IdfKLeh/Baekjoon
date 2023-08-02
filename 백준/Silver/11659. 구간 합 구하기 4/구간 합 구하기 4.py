import sys

num, additiontimes = map(int,sys.stdin.readline().split())
nums=[]
addition=[0]*(additiontimes*2)
sums =[0]*num
nums=list(map(int,sys.stdin.readline().split()))

for i in range(additiontimes):
    addition[i*2], addition[i*2+1]=map(int,sys.stdin.readline().split())

for i in range(num):
    if i ==0:
        sums[i]=nums[i]
    else:
        sums[i]=sums[i-1]+nums[i]

for i in range(additiontimes):
    answer=sums[addition[i*2+1]-1]
    if addition[i*2]==1:
        print(answer)
    else:
        answer-=sums[addition[i*2]-2]
        print(answer)
