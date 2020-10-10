class Node:
    def __init__(self, minne, antPros):
    # lager en konstrutør med minne og antall prosessorer
        self._minne = minne
        self._antPros = antPros

    def antaProsessorer(self):
    #returnere antall prosessorer
        return self._antPros

    def nokminne(self, paakrevdMinne):
        if self._minne >= paakrevdMinne:
            return True
        else:
            return False
