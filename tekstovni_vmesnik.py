from didzeridu import Zbirka
from datetime import datetime

zbirka = Zbirka()
#cas_vnosa = datetime.now()
#vrne (leto, mesec, dan, ura, minute, sekunde, ...)


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
        try:
            print(80 * '~')
            print('Kaj bi rada naredila?')
            moznosti = [
                ("nov vnos", vnesi_izvajalca),
                ("pokaži izvajalce", pokazi_izvajalce),
                ("pokaži albume", pokazi_albume)
            ]
            print('1.) Nov vnos')
            print('2.) Seznam izvajalcev')
            print('3.) Seznam albumov')
            print(80 * "-")
            vnos = input('> ')
            if vnos == '1':
                print('No, potem pa dajmo.')
                vnesi_izvajalca()
                #Treba bo še shranit podatke v json
                input("Pritisnite Enter za shranjevanje in vrnitev v osnovni meni...")
            elif vnos == '2':
                pokazi_izvajalce()
            elif vnos == '3':
                pokazi_albume()
            print()
        except KeyboardInterrupt:
            print()
            print("Nasvidenje!")
            return

def shrani_vnos(izvajalec, album):
    pass

def vnesi_izvajalca():
    vnos_izvajalca = input('Izvajalec: ')
    print(f'Super! \'{vnos_izvajalca}\' je dodan/a!')
    vnos_albuma = input('Album: ')
    print(f'Super, \'{vnos_albuma}\' je dodan!')
    vnos_leta = input('Leto izida: ')
    if vnos_leta == '':
        leto_izida = None
    else:
        leto_izida = vnos_leta
        print(f'Si bom zapomnil. Izdano leta {vnos_leta}')
    vnos_zanra = input('Če želiš, lahko dodaš tudi žanre (loči jih z vejico).\n'
        'Če ne veš, med katerimi lahko izbiraš, si oglej razdelek "Žanri": \n')
    if vnos_zanra == '':
        print('No, potem pa nič')
    else:
        print(f'Velja, {vnos_zanra} dodani med podatke o žanru. Hvala za trud!')
    cas_vnosa = datetime.now()
    celoten_vnos = (vnos_izvajalca, vnos_albuma, vnos_zanra, leto_izida, cas_vnosa)
    zbirka.dodaj_vnos(celoten_vnos)

tekstovni_vmesnik()