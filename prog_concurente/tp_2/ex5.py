import os, sys, time

N = int(sys.argv[1])

for i in range(N):
    pid = os.fork()
    
    if pid > 0:
        pid_fils, etat = os.wait()
        print(pid_fils)
        print(etat)
    
    else:
        print(os.getpid())
        print(os.getppid())
        time.sleep(2*i)
        sys.exit(i)
    