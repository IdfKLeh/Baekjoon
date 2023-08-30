import math
N= int(input())
fact = str(math.factorial(N))
answer=0
for i in fact[::-1]:
    if i=='0':
        answer+=1
    else:
        break
print(answer)

#알아 둘 것:
#슬라이싱 : [시작:끝:규칙]의 문법이다. 마지막에 -1을 넣었기 때문에 역순으로 프린팅
#math 라이브러리엔 factorial이 있다.
