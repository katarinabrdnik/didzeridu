import bottle
from didzeridu import Zbirka
from datetime import datetime


DATOTEKA_S_STANJEM = "stanje.json"

try:
    zbirka = Zbirka()
    zbirka.nalozi_stanje('stanje.json')
except FileNotFoundError:
    zbirka = Zbirka()

def shrani_stanje():
    zbirka.shrani_stanje('stanje.json')


@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovna_stran.tpl')

@bottle.post('/nov-vnos/')
def dodaj_nov_vnos():
    bottle.template('nov_vnos.tpl')
    izvajalec = bottle.request.forms.getunicode('izvajalec')
    album = bottle.request.forms.getunicode('album')
#    zanri = bottle.request.forms['žanri']
    leto_izida = bottle.request.forms.getunicode('leto izida')
    if izvajalec:
        vnos = (izvajalec, album, leto_izida, datetime.now())
        zbirka.dodaj_vnos(vnos)
        bottle.redirect('/')
    else:
        return 'Ne, če ne vneseš izvajalca! >:('

#@bottle.get('/nova-igra/')
#def novi_vnos():
#    return bottle.template


bottle.run(reloader=True, debug=True)