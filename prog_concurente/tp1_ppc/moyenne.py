import sys

moyenne = 0
flag = 1

sys.argv.pop(0)

if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        if flag = 1:
            sys.argv[i] = int(sys.argv[i])

            if 0 <= sys.argv[i] <= 20:
                moyenne += sys.argv[i]
        
        else:
            print("La note: ", sys.argv[i], "n'est pas valide")

    moyenne = moyenne/len(sys.argv)
    print("Moyenne = ", moyenne)

else:
    print("Aucune moyenne à calculer")
