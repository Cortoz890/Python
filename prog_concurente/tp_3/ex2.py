import sys, os

fichier = sys.argv[1]
(dfr, dfw) = os.pipe()

pid = os.fork()

if pid == 0:
    os.close(dfr)
    os.dup2(dfw, 1)
    os.close(dfw)
    dfw = os.execlp("sort", "sot", fichier)

else:
    os.close(dfw)
    os.dup2(dfr, 0)
    os.close(dfr)
    dfr = os.execlp("grep", "grep", "chaine")

sys.exit(0)