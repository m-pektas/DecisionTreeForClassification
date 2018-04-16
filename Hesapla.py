

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



    #kenarlardan biri direk yaprağa bağlanıyorsa yaprağın değerini döndür bağlanmıyorsa "düğüm" döndür.
    def yaprakBul(self,kenar,hedefKolonunDegerleri,sinifinSayilari):
        YaprakVarIse = []
        for j in hedefKolonunDegerleri:
            if sinifinSayilari[j] != 0:
                YaprakVarIse.append(j)

        if len(YaprakVarIse) == 1:
            return YaprakVarIse[0]
        else:
            return "Dügüm"


    #ağaç oluşturur.
    def CreateTree(self,root,data):

        level=None

        #kökte gez
        for i in root.kenarlarim:
            #direk yaprağa bağlanıyorsa bağla bağlanmıyorsa "düğüm" değerini ata
            x = self.yaprakBul(kenar=i,hedefKolonunDegerleri=root.HedefKolonumunDegerleri,sinifinSayilari=i.sinifiminSayilariSozluk)
            i.targetNode=x
            print("\nYaprak sa değeri değilse düğüm yaz :",x)

            newData = data[data[root.isim] == i.isim]  # root niteliğinin i kenarına göre veriyi filtreledim.
            newData = newData.reset_index(drop=True)
            print("\nNew Data : \n", newData)
            print("\nSözlük:",i.sinifiminSayilariSozluk)


