from turtle import st


class Prveks:
    def __init__(self, cislo: int, dalsi: "Prveks" | None):
            self.cislo = cislo
            self.dalsi = dalsi

class Spseznam():
    def __init__(self) -> None:
        self._hlava : Prveks | None = None

        def is_empty(self):
            return self._hlava is None
        
        def prepend(self, nove_cislo : int):
            staryprvni = self._hlava
            self._hlava = Prveks(nove_cislo, staryprvni)
        
        def get(self, idx):
            acc = 0
            if self.is_empty():
                raise Exception('prazdny bruh')
            aktualni = self._hlava
            while acc<idx:
                aktualni = aktualni.dalsi
                acc+=1
            return aktualni
        def pop_last(self):
            ...

