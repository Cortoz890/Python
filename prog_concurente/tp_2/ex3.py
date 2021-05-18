import os

pid1 = os.fork()

if pid1 == 0:
    pid2 = os.fork()
    
    if pid2 == 0:
        os.execlp("who", "who")
    
    else:
        os.wait()
        os.execlp("ps", "ps")

else:
    os.wait()
    os.execlp("ls", "ls" ,"l")
