from node import Node
class Rack:
    def __init__(self):
        # oppretter en konstrutør med en tom liste med noder
        self._noder = []
    def settInn(self, node):
    # legge til noder i listen
        self._noder.append(node)
    def hentNoder(self):
        # returnere listen
        return self._noder
    def getAntNoder(self):
        # finne antall noder i listen
        return len(self._noder)

        
    def _antaProsessorer(self):
        # øker antall prosessorer
        antall = 0
        for node in self._noder:
            antall += node.antaProsessorer()
        return antall


    def noderMedNokMinne(self,paakrevdMinne):
        # finne antall noder med nok minne
        tell = 0
        for node in self._noder:
            if node.nokminne(paakrevdMinne):
                tell += 1
        return tell
