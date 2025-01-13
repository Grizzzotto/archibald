import time
import sys
start = time.time()
sys.setrecursionlimit(10**7)
def facktorial(n):
    if n == 0:
        return 1
    else:
        return facktorial(n - 1)*n

def wait_seconds(n):
    for i in range(n):
        for i in range(30):
            facktorial(16900)

wait_seconds(10)
end = time.time()

print(end - start)