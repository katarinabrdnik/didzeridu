from didzeridu import Izvajalec, Zbirka
from datetime import datetime

zbirka = Zbirka()
#cas_vnosa = datetime.now()
#vrne (leto, mesec, dan, ura, minute, sekunde, ...)

def osnovni_zaslon():
    print('1.) Nov vnos')
    print('2.) Seznam izvajalcev')
    print('3.) Seznam albumov')
    vnos = input('> ')
    if vnos == '1':
        print('No, potem pa dajmo.')
        vnesi_izvajalca()
    elif vnos == '2':
        pokazi_izvajalce()
    elif vnos == '3':
        pokazi_albume()

def pokazi_izvajalce():
    for x in zbirka.seznam_izvajalcev():
        print(x)

def pokazi_vnose():
    for x in zbirka.seznam_vnosov():
        print(x)

def pokazi_albume():
    for vnos in zbirka.seznam_vnosov():
        izvajalec = vnos[0]
        album = vnos[1]
        print(f'{album} ({izvajalec})')

def uvodni_pozdrav():
    print('Hojla, Katarina! Kako gre? V redu? :)')

def tekstovni_vmesnik():
    uvodni_pozdrav()
    while True:
        osnovni_zaslon()

def shrani_vnos(izvajalec, album):
    pass

def vnesi_izvajalca():
    vnos1 = input('Izvajalec: ')
    print(f'Super! \'{vnos1}\' je dodan/a!')
    vnos2 = input('Album: ')
    print(f'Super, \'{vnos2}\' je dodan!')
    cas_vnosa = datetime.now()
    celoten_vnos = (vnos1, vnos2, cas_vnosa)
    zbirka.dodaj_vnos(celoten_vnos)

tekstovni_vmesnik()
