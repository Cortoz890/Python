import os

for i in range(3):
    pid = os.fork()
    print("(i: ", i, ") je suis le processus: ", os.getpid(), "mon pere est: " , os.getppid(), "le code de retour est: ", pid)
    

   




