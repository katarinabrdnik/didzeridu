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

    def slovar_s_stanjem(self):
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
        return vnos_v_slovar
#vnos se shrani v nabor oblike celoten_vnos = (vnos_izvajalca, vnos_albuma, vnos_zanra, leto_izida, cas_vnosa)
    @classmethod
    def slovar_v_nabor(cls, slovar, kljuc):
        zbirka = cls()
        vnosi = slovar[kljuc]
        seznam_naborov = [tuple(vnos.values()) for vnos in vnosi]
        return seznam_naborov

    def shrani_stanje(self, datoteka):
        with open(datoteka, "w", encoding="utf-8") as file:
            json.dump(self.slovar_s_stanjem(), file, ensure_ascii=False, indent=4)

#    @classmethod
#    def nalozi_iz_slovarja(cls, slovar_s_stanjem):
#        zbirka = cls()
#        for vnos in slovar_s_stanjem["vnosi"]:           
#        return zbirka

    def nalozi_stanje(cls, datoteka):
        with open(datoteka) as file:
            slovar_s_stanjem = json.load(file)
        return cls.slovar_v_nabor(slovar_s_stanjem, "vnosi")
