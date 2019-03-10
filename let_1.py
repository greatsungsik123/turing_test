a = int(input())

b = input()

b = b.split(" ")
for i in range(len(b)):

    b[i] = int(b[i])

for i in range(len(b)):
    for j in range(len(b)-1 ):
        if(b[j] > b[j]):

            b[j],b[j+1] = b[j+1],b[j]
n = 0
m = 0
for x in range(len(b)):

    m = m + b[i]
    n  = n + m

print(n)
"""
질문
"""