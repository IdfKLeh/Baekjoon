import sys

money,people = sys.stdin.readline().split()
money = int(money)
people = int(people)

print(money//people)
print(money%people)