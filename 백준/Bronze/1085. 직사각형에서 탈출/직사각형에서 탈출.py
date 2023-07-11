import sys
x ,y, w, h = sys.stdin.readline().split()
x=int(x)
y=int(y)
w=int(w)
h=int(h)
least = x
if(y<least):
    least = y
if(w-x<least):
    least = w-x
if(h-y<least):
    least = h-y

print(least)
