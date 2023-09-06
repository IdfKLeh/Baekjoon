import sys

K= int(input())
isgoingtoadd=[]
for _ in range(K):
  target = int(sys.stdin.readline())
  if target==0:
    isgoingtoadd.pop()
  else:
    isgoingtoadd.append(target)
  
print(sum(isgoingtoadd))