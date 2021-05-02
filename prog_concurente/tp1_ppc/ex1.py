import sys

print("Nom du programme : ", sys.argv[0])
print("Nombre d'arguments : ", len(sys.argv) - 1)
print("Les arguments sont : ")

print(sys.argv[2])

for arg in sys.argv[1:]:
    print(arg)

