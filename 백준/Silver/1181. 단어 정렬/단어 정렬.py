import sys
N = int(input())

words = [sys.stdin.readline().rstrip() for _ in range(N)]

answer=list(set(words))

answer.sort(key=lambda x:(len(x),x ))

for i in range(len(answer)):
    print(answer[i])

#집중해서 볼 것: answer.sort(key=lambda x:(len(x),x )), answer=list(set(words))
#sort함수에 key를 주면 그 키를 토대로 정렬하는데, 여기에 람다를 사용하여
#lambda 매개변수 : 표현식 의 형태로 한줄로 함수를 쓰게 해줌
#여기선 len을 먼저 적용시켜 정렬하되, 길이가 같은 경우 x를 이용하여 알파벳 순으로 정렬해줌.
#람다를 공부하자.

#list(set(words))의 경우 리스트를 set으로 바꿨다가 다시 리스트로 바꿔서 set에선 중복이 허용되지 않는 것을 이용해 중복들을 없앰
#그러나 주의할 점은 set으로 바꾸는 과정에서 리스트의 순서가 바뀌기 때문에, 주의하고 사용할 것.