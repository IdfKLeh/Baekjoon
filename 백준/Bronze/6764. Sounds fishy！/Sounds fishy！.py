import sys

fish = [0 for i in range(4)]

for i in range(4):
    fish[i] = int(sys.stdin.readline())

if fish[3]>fish[2] and fish[2]>fish[1] and fish[1]>fish[0]:
    print("Fish Rising")

elif fish[3]<fish[2] and fish[2]<fish[1] and fish[1]<fish[0]:
    print("Fish Diving")

elif fish[3]==fish[2] and fish[2]==fish[1] and fish[1]==fish[0]:
    print("Fish At Constant Depth")

else:
    print("No Fish")