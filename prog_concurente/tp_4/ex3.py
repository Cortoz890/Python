import signal, time, sys, os

fin = False

def stop(signal, frame):
    global fin
    fin = True
    print("C'est l'heure d'arrêt")
    
signal.signal(signal.SIGINT, stop)

pid = os.fork()


while fin == False:
    time.sleep(1)
    print("ça boucle")


