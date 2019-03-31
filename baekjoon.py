"""
a = int(raw_input())

number = []

for x in range(a):

    b,c = map(int,raw_input().split(" "))

    number.append([b,c])


for i in range(a):
    print(number[i][1]-number[i][0]+2)
"""

d = 0
e = 0


a,b,c = map(int,raw_input().split())

d = b-a
e = c-b

if(d > e):
    print(d)
if(e > d):
    print(e)

