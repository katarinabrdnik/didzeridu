import json
class Zbirka:
    def __init__(self):
        self.izvajalci = []
        self.albumi = []
        self.vnosi = []

#    def dodaj_izvajalca(self, izvajalec):
#        self.izvajalci.append(izvajalec)
#
#    def dodaj_album(self, album):
#        self.albumi.append(album)

    def dodaj_vnos(self, vnos):
        self.vnosi.append(vnos)

    def odstrani_vnos(self, vnos):
        self.vnosi.remove(vnos)

    def seznam_izvajalcev(self):
        return [vnos[0] for vnos in self.vnosi]

    def seznam_albumov(self):
        return [vnos[1] for vnos in self.vnosi]

    def seznam_vnosov(self):
        return self.vnosi

    def slovar_s_stanjem(self, datoteka):
        vnos_v_slovar = {
            "vnosi": [
                {
                    "izvajalec": vnos[0],
                    "album": vnos[1],
                    "žanri": vnos[2],
                    "leto izida": vnos[3],
                    "čas vnosa": vnos[4]
                }
                for vnos in self.vnosi
            ]
        }
        with open(datoteka, "w", encoding="utf-8") as file:
            json.dump(vnos_v_slovar, file, ensure_ascii=False, indent=4)
#vnos se shrani v nabor oblike celoten_vnos = (vnos_izvajalca, vnos_albuma, vnos_zanra, leto_izida, cas_vnosa)