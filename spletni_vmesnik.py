import bottle
from didzeridu import Zbirka
from datetime import datetime, date

from itertools import groupby
from operator import itemgetter


DATOTEKA_S_STANJEM = "stanje.json"

#try:
#    Zbirka().nalozi_stanje(DATOTEKA_S_STANJEM)
#except FileNotFoundError:
#    zbirka = Zbirka()

#def shrani_stanje():
#    zbirka.shrani_stanje(DATOTEKA_S_STANJEM)
zbirka = Zbirka()

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovna_stran.tpl')
    
@bottle.post("/nov-vnos/")
def dodaj_nov_vnos():
    izvajalec = bottle.request.forms.getunicode('izvajalec')
    album = bottle.request.forms.getunicode('album')
    datum = date.today().strftime("%d-%m-%Y")
    zanri = 'rock'
    leto_izida = bottle.request.forms.getunicode('leto izida')
    nov_vnos = (izvajalec, album, zanri, leto_izida, datum)
    zbirka.dodaj_vnos(nov_vnos)
    zbirka.shrani_stanje(DATOTEKA_S_STANJEM)
    bottle.redirect("/")


#@bottle.get("/seznam-vnosov/")
##def tabela_vnosov():
#    moj_seznam_naborov = zbirka.nalozi_stanje(DATOTEKA_S_STANJEM)
#    cel_html = []
#    for name, rows in groupby(moj_seznam_naborov, itemgetter(0)):
#        table = []
#        for izvajalec, album, zanri, leto_izida, cas_vnosa in rows:
#            table.append(
#            f"<tr><td>{izvajalec}</td><td>{album}</td><td>{zanri}</td><td>{leto_izida}</td><td>{cas_vnosa}</td><td></tr>")
#        table = "<table>\n{}\n</table>".format('\n'.join(table))
#        cel_html.append(table)
#    cel_html = "<html>\n{}\n</html>".format('\n'.join(cel_html))
#    return cel_html


bottle.run(reloader=True, debug=True)