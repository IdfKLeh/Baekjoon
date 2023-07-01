
weight=[]
value=[]
things, max_weight = map(int,input().split())

for i in range(things):
    w, v = map(int,input().split())
    weight.append(w)
    value.append(v)

bag=[[0 for i in range(max_weight+1)] for j in range(things)]
for i in range(things):
    for j in range(max_weight+1):
        if i==0:
            if j>=weight[i]:
                bag[i][j]=value[i]
        else:
            bag[i][j]=bag[i-1][j]
            if j >=weight[i]:
                if bag[i][j]<bag[i-1][j-weight[i]]+value[i]:
                    bag[i][j] = bag[i-1][j-weight[i]]+value[i]

print(bag[things-1][max_weight])