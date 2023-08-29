import sys
K, N = map(int,sys.stdin.readline().split())

lans = [int(sys.stdin.readline())for i in range(K)]

left = 1 
right = max(lans)

def finding(left, right):
    while left<=right:
        answer = (left+right)//2
        cables = [i//answer for i in lans]
        if sum(cables)<N:
            right=answer-1
        else:
            left=answer+1
    
    return right
        
print(finding(left, right))

#알아야 할 것:
# cables = [i//answer for i in lans]: 이런식으로 새로운 리스트 만들기 가능. 전 리스트를 포문으로 돌리기.
#이중 탐색의 구조. left와 right가 있고, left가 right 보다 커지면 중단하며, right를 출력함.
#그리고 mid를 (left+right)//2로 잡은점을 기억하자.