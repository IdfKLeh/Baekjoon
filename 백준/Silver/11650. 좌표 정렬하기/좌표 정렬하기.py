import sys

N=int(input())


aray=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]

aray.sort(key=lambda x:(x[0], x[1]))

for i in aray:
  print(i[0],i[1])

#기억할 것: lambda의 활용방법. sort의 key 도 기억하면 좋고.
#list는 리스트 형식을 반환하기 때문에 []안에 안넣어도 된다.