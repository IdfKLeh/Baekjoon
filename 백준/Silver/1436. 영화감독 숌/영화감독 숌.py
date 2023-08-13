def checkif666in(string):
    for i in range(len(string)-2):
        if string[i] == '6' and string[i+1] == '6' and string[i+2] == '6':
            return True
    return False

N = int(input())

answer=666

while True:
    check = str(answer)
    if checkif666in(check):
        N-=1
    if N==0:
        break
    answer+=1

print(answer)

#def 함수이름(인자): 의 형태로 함수를 선언.
#사용전에 함수 선언 해야함.
#return이 나오면 함수 종료 됨.