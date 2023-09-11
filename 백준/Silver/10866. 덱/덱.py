import sys
N=int(input())
deque=[]
for i in range(N):
    command=sys.stdin.readline().rstrip()
    if command=='pop_front':
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop(0))
    elif command=='pop_back':
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop())
    elif command=='size':
        print(len(deque))
    elif command=='empty':
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif command=='front':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif command=='back':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])
    else:
        command,num=command.split()
        if command=='push_back':
            deque.append(num)
        else:
            deque.insert(0,num)

#pop 은 index, remove는 target num 을 지움. pop은 반환도 함.
#strip은 앞뒤의 공백, 개행문자를 지워줌. lstrip은 왼쪽만, rstrip은 오른쪽만.