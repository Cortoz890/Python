import os

name = "le pere"
pid = os.fork()

if pid == 0:
    name = "le fils"
    print("Je suis", name)

else:
    print("Je suis", name)
    os.wait

os._exit(0)