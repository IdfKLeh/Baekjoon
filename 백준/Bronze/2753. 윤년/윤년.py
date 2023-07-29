import sys
year = int(sys.stdin.readline())
isyoon=False
if year%4==0:
    if year%400==0 or year%100!=0:
        isyoon=True
    
if isyoon==True:
    print(1)
else:
    print(0)
    