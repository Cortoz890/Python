import os, sys

msg = "monMessage"
msg_byte = msg.encode("ascii")
print("Création d'un pipe anonyme")
(dfr, dfw) = os.pipe()
n = os.write(dfw, msg_byte)
print("Le processus %d a transmis le message %s\n" % (os.getpid(), msg_byte))
msgReçu = os.read(dfr, len(msg))
print("Le processus %d a reçu le message %s\n" %(os.getpid(), msgReçu))

os.close(dfr); os.close(dfw)
sys.exit(0)