import sys

line, brands = map(int, sys.stdin.readline().split())
cheap = 2000
bunches=[]
ones=[]
for i in range(brands):
    bunch, one = map(int, sys.stdin.readline().split())
    bunches.append(bunch)
    ones.append(one)

bunch=min(bunches)
one=min(ones)
if (one*6)>bunch:
    cut = bunch/one
    buyingbunches = line//6
    cheap = buyingbunches*bunch
    if cut>=line%6:
        cheap+=one*(line%6)
    else:
        cheap+=bunch
    
else:
    if cheap>one*line:
        cheap = one*line
    
print(cheap)