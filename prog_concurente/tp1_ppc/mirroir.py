import sys

L = []
Linv = []

sys.argv.pop(0)
print(sys.argv)

for i in range(len(sys.argv)):
    L.append(list(sys.argv[i]))
    Linv.append(list(sys.argv[i]))

print(L)

for j in range(len(L)):
    for i in range(len(L[j])):
        Linv[j][i] = L[j][-i - 1]
    

print(Linv)

