from regneklynge import Regneklynge
from node import Node
from rack import Rack

def hovedprogram():
# lager jeg regneklynge med plass til 12 noder
    ra = Regneklynge(12)
    for i in range(650) :
        ra.settInnNode(Node(64, 1))
    for i in range(16):
        ra.settInnNode(Node(1024,2))

    print('Noder med minst 32 GB: ', ra.noderMedNokMinne(32))
    print('Noder med minst 64 GB: ', ra.noderMedNokMinne(64))
    print('Noder med minst 128 GB: ', ra.noderMedNokMinne(128))


    print('Antall prosessorer: ', ra.antProsessorer())
    print('antal racks : ', ra.antRacks())
    print()


hovedprogram()


'''def stor (a,b,c):
    if a>b and a>c:
        svar= a
        print(svar)
    elif b>a and b>c:
        svar = b
        print(svar)
    else:
        print(c)

stor(5,3,5)

def pris(gratis, alder):
    if gratis == True:
        return 0
    elif gratis == False:
        if alder < 18:
            return 100
        else:
            return 200
print(pris(False, 2))

print (False or False)

x = ''
for i in range(1,99,2):
    if i == 55:
        continue
    x += '*'
    print(x)
d = bin(900)
print(d)


liste1 = [1,2,3,9,4,5,6,6,7]
def sortert(liste):
    x = 0
    for i in liste:
        while i >= x:
            x = i
        else:
            return False
print(sortert(liste1))'''
