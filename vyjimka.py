mapa = {}
def drm_opt(a, mapa):
    if a in mapa:
        return mapa[a], 'from cache'
    else:
        k = drm(a)
        mapa[a] = k
        return k

def drm(a):
    if a >= 0:
        return a**(1/2)
    else:
        raise Exception('bruh')

print(drm_opt(4, mapa))
print(drm_opt(4, mapa))
print(drm_opt(4, mapa))
print(drm_opt(16, mapa))
print(drm_opt(16, mapa))
print(drm_opt(-16, mapa))
