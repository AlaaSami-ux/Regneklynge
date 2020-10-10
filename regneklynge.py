from rack import Rack
from node import Node
class Regneklynge:
    # konstrukt�ren tar inn antall noder per rack.
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._rack = []


    def settInnNode(self, node):
        # sjekker hvis det er ledig plass inn i rack og hvis ikke oppretter jeg en ny
        if len(self._rack) == 0:
            self._rack.append(Rack())
            self._rack[0].settInn(node)
        else:
            for rack in self._rack:
                if rack.getAntNoder() < self._noderPerRack:
                    rack.settInn(node)
                elif self._rack.index(rack) == len(self._rack) -1:
                    self._rack.append(Rack())

    def antProsessorer(self):
    # Beregner totalt antall prosessorer i hele regneklyngen og returnere det.
        antallP = 0
        for i in self._rack:
            antallP += i._antaProsessorer()
        return antallP

    def noderMedNokMinne(self, paakrevdMinne):
        # Beregner antall noder i regneklynge
        tell = 0
        for rack in self._rack:
            for node in rack.hentNoder():
                if node.nokminne(paakrevdMinne):
                    tell += 1
        return tell

    def antRacks(self):
        # finne antall racks i regneklynge
        return len(self._rack)
