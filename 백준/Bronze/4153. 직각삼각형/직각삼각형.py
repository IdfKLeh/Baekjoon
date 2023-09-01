import sys
tri= [0]
inpu = list(map(int,sys.stdin.readline().split()))
while inpu !=[0,0,0]:
    tri.append(inpu)
    inpu = list(map(int,sys.stdin.readline().split()))
answer=[0]
for i in tri[1:len(tri)]:
    i.sort()
    if i[0]*i[0]+i[1]*i[1]==i[2]*i[2]:
        answer.append('right')
    else:
        answer.append('wrong')
for i in answer[1:]:
    print(i)

#되는게 신기한 끔찍한 코드.
#우선 inpu를 tri에 리스트 형태로 그냥 집어넣어버려서, tri를 2차원 배열로 만들 수 있다는 걸 기억하자.
#그리고 append를 통해 리스트를 만들었기 때문에, 0번이 아닌 스타팅을 1번부터 잡음.
#그냥 너무 보기 안좋다ㅠ