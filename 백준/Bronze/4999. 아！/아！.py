import sys
ahs = [sys.stdin.readline() for i in range(2)]
if len(ahs[0])>=len(ahs[1]):
    print("go")
else:
    print("no")