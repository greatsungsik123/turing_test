
a = input()



camp = ["C","A","M","B","R","I","D","G","E"]

c = True

comp = []

for x in range(len(a)):

    c = True

    for i in range(len(camp)):

        if(a[x] == camp[i]):

            c = False

    if(c == True):
        comp.append(a[x])



comp = "".join(comp)

print(comp)

