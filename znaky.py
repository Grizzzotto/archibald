import time
mapa = {}
def cerzel_opt(a, mapa):
    if a in mapa:
        return mapa[a]
    else:
        k = cerzel(a)
        mapa[a] = k
        return k
def cerzel(a):
    a.upper()
    b =0
    i = 0
    for i in range(len(a)):
        b += ord(a[i])
        i += 1
    if b % 2 == 0:
        return 1
    else:
        return 0
    
    


start1 = time.time()

for i in range(100000000):
    cerzel_opt('qwertyuiop', mapa)
end1 = time.time()
print(end1 - start1)
start2 = time.time()
for i in range(100000000):
    cerzel('qwertyuiop')
end2 = time.time()

print(mapa)
print(end2 - start2)





