import os, sys
import random as r

N = 100
(dfr1, dfw1) = os.pipe()
(dfr2, dfw2) = os.pipe()
pid = os.fork()

for i in range(N+1):
    nbr = r.randint(0, 9)

    if pid == 0:
        if nbr % 2 == 0:
            os.write(dfw1, str.encode(str(nbr )))
            

    else:
        if nbr % 2 != 0:
            os.write(dfw2, str.encode(str(nbr )))
            


os.write(dfw1, str.encode(str(-1)))
os.write(dfw2, str.encode(str(-1)))

paire = os.read(dfr1, N)
paire.decode()
impaire = os.read(dfr2, N)
impaire.decode()

print(paire)
print(impaire)