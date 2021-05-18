import signal, time, sys, os

def stop(signal, frame):
    print("Le fils reçoit le signal")
    sys.exit(0)
    

pid = os.fork()

if pid == 0:
    signal.signal(signal.SIGINT, stop)

    while True:
        time.sleep(1)
        print("Le fils boucle")


if pid > 0:
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    for i in range(6):
        time.sleep(1)
        print("Le père boucle pour la ", i, "éme fois")
        
