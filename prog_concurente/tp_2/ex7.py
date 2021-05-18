import os, sys

N = 3

for i in range(N):
    pid1 = os.fork()
    pid2 = os.fork()

print("Chanteee")
sys.exit(0)