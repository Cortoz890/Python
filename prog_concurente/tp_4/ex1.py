import signal, time, sys

def stop(signal, frame):
    print("C'est l'heure d'arrêt")
    sys.exit(0)

signal.signal(signal.SIGINT, stop)

while True:
    time.sleep(1)
    print("ça boucle")
    
    
