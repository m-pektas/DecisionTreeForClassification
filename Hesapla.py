

#Bu sınıf gerekli matematiksel hesaplamaların yapıldığı sınıftır.
from math import log2

class HesapMakinesi:
    #Verilen niteligin entropisinin ağırlıklı ortalamasını bulur
    def genelEntropiHesapla(self,hdfNit):
        degerlerSozlugu = hdfNit.kenarlariminSayilari
        toplamKayıtSayisi = len(hdfNit.kolonHalim)
        sonuc=0

        for i in hdfNit.kenarlarim:
            x = degerlerSozlugu[i.isim]/toplamKayıtSayisi
            sonuc = sonuc + ((-x)*log2(x))

        return sonuc

    def kazancHesapla(self,genelEntropi,NitEntropi):
        sonuc = genelEntropi-NitEntropi
        return sonuc

    def agirlikliEntropiBul(self,nitelik):
        kenarlar = nitelik.kenarlarim
        toplamKayitSayisi = len(nitelik.kolonHalim)
        hedefNiteliginAyrikDegerleri = nitelik.HedefKolonumunDegerleri
        sonuc = 0
        for i in kenarlar:
            for j in hedefNiteliginAyrikDegerleri:
                a = i.sinifiminSayilariSozluk[j]
                if a == 0:
                    entropi = 0
                else:
                    s = i.toplamSayim
                    r = a/s
                    agirlik = s/toplamKayitSayisi
                    entropi = (-r) * log2(r)

                sonuc = sonuc + (agirlik * entropi) #agırlıklı entropi hesaplandı.

        return sonuc





