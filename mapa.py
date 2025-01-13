from random import randint
tel = {}
tel['0405253498'] = 'jan novak'
tel['0987643321'] = ' qwertyu'

print(tel.get('0405253498'))
for i in range(1000):
    tel[f'{randint(1000000000, 9999999999)}'] = f'mister {randint(0, 99999999)}'
print(tel)


'''
v 29
o 19
l 15
o 19
k 14
i 12
t 26
i 12 
n 17 
'''