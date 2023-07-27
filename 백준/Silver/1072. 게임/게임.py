
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
"""
여기 아래 부터는 내가 짠 코드인데,
아마도 부동 소수점 어쩌고 때문에 오류가 나는듯 하다.
88프로까지는 성공하거든.
import sys

finished, won = map(int, sys.stdin.readline().split())
percentage = (100*won)//finished
left=0
right=1000000000
answer = (finished-won)//2
if percentage>=99:
    print(-1)
    exit()

while(True):
    answer=(left+right)/2
    if answer%1!=0:
        answer+=0.5
    target = 100*(won+answer)//(finished+answer)
    if left== answer-1:
        if target==percentage+1:
            break
        else:
            answer +=1
            break
    if target>=percentage+1:
        right=answer
    elif target<percentage+1:
        left=answer
    
    


print(int(answer))
"""