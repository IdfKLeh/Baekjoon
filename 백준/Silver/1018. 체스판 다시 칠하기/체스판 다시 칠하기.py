import sys

m, n = map(int,sys.stdin.readline().split())

theboard = [list(sys.stdin.readline().rstrip()) for i in range(m)]
answers = [[0]*(n-7) for i in range(m-7)]
white = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
black=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
whitenum=0
blacknum=0

for i in range(m-7):
    for j in range(n-7):
        for y in range(8):
            for x in range(8):
                if theboard[i+y][j+x] != white[y][x]:
                    whitenum+=1
                if theboard[i+y][j+x] != black[y][x]:
                    blacknum+=1
        answers[i][j]=min(whitenum, blacknum)
        whitenum=0
        blacknum=0
print(min(map(min,answers)))