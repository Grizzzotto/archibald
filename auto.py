

class Auto:
    def __init__(self, vyrobce, model, objem, vykon):
        self._vyrobce = vyrobce
        self._model = model
        self._objem = objem
        self._vykon = vykon



    def __eq__(self, other):
        if isinstance(other, Auto):
            return self._vyrobce==other._vyrobce and self._model== other._model and self._objem == other._objem and self._vykon == other._vykon
        else:
            return False

a1 = Auto('bmv', 'x5', 1, 100)
a3 = Auto('bmv', 'x5', 1, 100)
a2 = Auto('ford', 'x6', 2, 200)

if a1 == a3:
    print('stejne')
else:
    print('jine')