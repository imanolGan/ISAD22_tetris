#konektar con datubase
import view.db

class Erabiltzailea:

    def __init__(self):
        #self.izena = izena
        #self.pasahitza=pa
        self. konektatuta= False
        self.saiakerak=3

    #def erabiltzailea_erregistratu(self):

    def saioa_hasi(self, izena, pas):
        pasahitza=view.db.erab_pasahitza_lortu(izena)
        print(self.saiakerak)
        if pas is None:
            print("Ez da pasahitzik sartu")
        else:
            if pasahitza is not None and self.saiakerak>0 :
                pas1=str(pasahitza)
                pasahitza = pas1[2:len(pas1) - 3]
                pasahi = pas
                print(pasahitza)
                print(pasahi)
                print(pasahitza == pasahi)
                print("ERAB PASAHITZA")
                if pasahi == pasahitza:
                    self.konektatuta = True
                    print("Erabiltzailea konektatu da")
                else:
                    self.saiakerak -= 1
        print(pasahitza)
        print("SAIOA HASI")

        if self.saiakerak==0:
            print("Errorea: pasahitza ez da zuzena")
        return self.konektatuta

    def erab_badag(self,izena):
        print("ERAB")
        print(izena)
        ema= view.db.erab_badago(izena)
        return ema

    def saiakera_badu(self):
        return self.saiakerak>0

    def saioa_bukatu(self):
        self.konektatuta=False
        self.saiakerak=3
        print("Saioa itxi duzu")

    def erab_gehitu (self, izena, pasah, gal1, gald2):
        print("ERABIL--> ERAB_GEHITU")
        ema=view.db.erabGehitu(izena, pasah, gal1, gald2)
        print(ema)

    def galderaZuzenak(self,izena, gal1,gal2):
        zuzena=False
        em=view.db.erab_gald_lortu(izena,1)
        erantz1= str(em)
        em=erantz1[2:len(erantz1) - 3]
        print(erantz1)
        print(em)
        print(gal1)
        print("GALDE ZUZ")
        if em == gal1:
            print("SART")
            em = view.db.erab_gald_lortu(izena,2)
            erantz1 = str(em)
            em = erantz1[2:len(erantz1) - 3]
            print(em)
            if em==gal2:
                zuzena=True
        return zuzena

    def pasahAld(self, izena, pa):
        print(pa)
        view.db.updatePasah(izena,pa)
        aldatu=False
        em=view.db.erab_pasahitza_lortu(izena)
        er=str(em)
        em=er[2:len(er) - 3]
        if em == pa:
            aldatu=True
        print(aldatu)
        return aldatu