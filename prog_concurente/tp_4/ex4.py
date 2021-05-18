import signal, time, sys, os

fin = False

def stop(signal, frame):
    global fin
    fin = True
    print("C'est l'heure d'arrêt")
    
signal.signal(signal.SIGINT, stop)

pid = os.fork()

if pid == 0:
    while fin == False:
        time.sleep(1)
        print("Le fils boucle")


if pid > 0:
    for i in range(6):
        print("Le père boucle pour la ", i, "éme fois")
        time.sleep(1)
        if i == 3:
            os.kill(pid, signal.SIGKILL)
            print("signal envoyé")
