import sys
a, b,c,d,e=map(int,sys.stdin.readline().split())
sum = a*a+b*b+c*c+d*d+e*e
print(sum%10)