import json
class Zbirka:
    def __init__(self):
        self.vnosi = []

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

    def v_slovar(self):
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
    
    @staticmethod
    def iz_slovarja(slovar):
        zbirka = Zbirka()
        zbirka.vnosi = [
            Zbirka.iz_slovarja(sl_vnosa) for sl_vnosa in slovar["vnosi"]
        ]
        return zbirka

    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Zbirka.iz_slovarja(slovar)
