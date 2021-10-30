import bottle
from didzeridu import Zbirka
from datetime import datetime

zbirka = Zbirka()

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('views/osnovna_stran.tpl')

@bottle.get('/nov-vnos/')
def dodaj_nov_vnos():
    bottle.template('views/nov_vnos.tpl')
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