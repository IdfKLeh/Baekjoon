import sys

finished, won = map(int, sys.stdin.readline().split())
percentage = (100*won)//finished
left=0
right=finished
answer = (left+right)//2
if percentage>=99:
    real = -1
else:
    while left<=right:
        answer = (left+right)//2
        target = 100*(won+answer)//(finished+answer)
        if target > percentage:
            real = answer
            right = answer-1
        else:
            left= answer+1


print(real)