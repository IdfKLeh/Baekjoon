N = input()
num=int(N)
answer=0
if (len(N)*9)>=num:
    target=0
else:
    target = num-(len(N)*9)

while(target<=num):
    sum=0
    for i in str(target):
        sum+=int(i)
    if (target+sum)==num:
        answer=target
        break
    else:
        target+=1
print(answer)


