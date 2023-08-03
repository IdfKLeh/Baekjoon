import sys

people = int(sys.stdin.readline())
friends = [["N" for i in range(people)] for i in range(people)]
actual = [["N" for i in range(people)] for i in range(people)]
answers=[0]*people
for i in range(people):
    friends[i] = list(sys.stdin.readline().rstrip())
    actual[i]= list(friends[i])

for i in range(people):
    for j in range(people):
        if friends[i][j]=="Y":
            for _ in range(people):
                if friends[j][_]=="Y":
                    actual[i][_]="Y"
    actual[i][i]="N"

for i in range(people):
    for j in range(people):
        if actual[i][j]=="Y":
            answers[i]+=1

print(max(answers))


