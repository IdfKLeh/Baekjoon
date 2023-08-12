import sys
nums=[]
while True:
    num = sys.stdin.readline().rstrip()
    if num =='0':
        break
    nums.append(list(num))



for i in range(len(nums)):
    answer='yes'
    for j in range(len(nums[i])//2):
        if nums[i][j] != nums[i][-j-1]:
            answer = 'no'
    print(answer)

#주의 깊게 볼 것:
#첫 문단처럼 2차원 배열 선언 이후 하나씩 채우기 위해서는,
#걍 저런식으로 빈배열 만든 다음 append로 리스트를 넣어버리면 된다.
