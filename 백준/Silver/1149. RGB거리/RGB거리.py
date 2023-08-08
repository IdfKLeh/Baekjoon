import sys
numberofhouses = int(sys.stdin.readline())
cost=[list(map(int,sys.stdin.readline().split()))for _ in range(numberofhouses)]
answer = [[0]*3 for i in range(numberofhouses)]

answer[0] = cost[0]

for i in range(1,numberofhouses):
    answer[i][0] = cost[i][0]+min(answer[i-1][1], answer[i-1][2])
    answer[i][1] = cost[i][1]+min(answer[i-1][0], answer[i-1][2])
    answer[i][2] = cost[i][2]+min(answer[i-1][0], answer[i-1][1])

print(min(answer[-1]))

#여기서 주의깊게 볼 것: cost를 만들때 list와 for문을 사용한 방법,
#   answer를 만들때 2차 배열을 깔끔하게 만든 것
#   그리고 Dp는 전에 구한 값을 배열에 저장, 다음값을 구하는 데에 사용하는 방법이다.z