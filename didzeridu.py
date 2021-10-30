#res se bom potrudila to naredit čim bolj kul

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

    def seznam_izvajalcev(self):
        return [vnos[0] for vnos in self.vnosi]

    def seznam_albumov(self):
        return [vnos[1] for vnos in self.vnosi]

    def seznam_vnosov(self):
        return self.vnosi



