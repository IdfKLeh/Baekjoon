import sys
A, B, V = map(int,sys.stdin.readline().split())

if (V-A)/(A-B)>(V-A)//(A-B):
    print((V-A)//(A-B)+2)
else:
    print((V-A)//(A-B)+1)
