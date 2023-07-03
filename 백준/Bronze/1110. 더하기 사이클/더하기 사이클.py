import sys

num=[]
firstnum=[0,0]

cycle=0
input = int(sys.stdin.readline())
firstnum[0]=input//10
firstnum[1]=input%10
num=firstnum.copy()
while(True):
    cycle=cycle+1
    newnum=num[0]+num[1]
    num[0]=num[1]
    num[1]=newnum%10
    if num==firstnum:
        break



print(cycle)

