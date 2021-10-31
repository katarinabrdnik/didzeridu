import bottle
from didzeridu import Zbirka
from datetime import date
from tabulate import tabulate


DATOTEKA_S_STANJEM = "stanje.json"

zbirka = Zbirka()

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovna_stran.tpl')
    
@bottle.post("/nov-vnos/")
def dodaj_nov_vnos():
    izvajalec = bottle.request.forms.getunicode('izvajalec')
    album = bottle.request.forms.getunicode('album')
    datum = date.today().strftime("%d-%m-%Y")
    zanri = ''
    for checkbox in 'Rock', 'Metal', 'Folk', 'Hip hop', 'Alternativa', 'Pop', 'Eksperimentalna', \
        'Jazz', 'R&B', 'Klasična', 'Blues', 'Elektronska', 'Plesna', 'Punk', 'Govorjena beseda', 'Drugo':
        vrednost = bottle.request.forms.get(checkbox)
        if vrednost:
            zanri += f'{checkbox}, '
    leto_izida = bottle.request.forms.getunicode('leto izida')
    nov_vnos = (izvajalec, album, zanri, leto_izida, datum)
    zbirka.dodaj_vnos(nov_vnos)
    zbirka.shrani_stanje(DATOTEKA_S_STANJEM)
    bottle.redirect("/")

@bottle.get("/seznam-vnosov/")
def tabela_vnosov():
    seznam = [['Izvajalec', 'Album', 'Žanri', 'Leto izida', 'Dan vnosa']]
    for vnos in zbirka.seznam_vnosov():
        seznam.append(list(vnos))
    return tabulate(seznam, tablefmt='html')


bottle.run(reloader=True, debug=True)