number = int(input())


temp = input()
a = temp.split(" ")



for i in range(len(a)):
    a[i] = int(a[i])


temp = input()


b = temp.split(" ")

for i in range(len(b)):
    b[i] = int(b[i])


for i in range(len(a)):

        for x in range(len(a) - 1):

            if (a[x] < a[x + 1]):
                a[x], a[x + 1] = a[x + 1], a[x]

for z in range(len(a)):


        for c in range(len(a) - 1):

            if (b[c] > b[c + 1]):
                b[c], b[c + 1] = b[c + 1], b[c]

qwerty = 0

for i in range(len(a)):
    qwerty = qwerty + (a[i] * b[i])
print(qwerty)
















































































































































