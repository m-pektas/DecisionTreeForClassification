
#Bu sınıf gerekli matematiksel hesaplamaların yapıldığı sınıftır.
from math import log2
from Nitelik import Nitelik


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
    def CreateTree(self,root,hedefNitelikAdi,nitelikler):
        nitelikler.remove(root.isim)

        level = []
        level.append(root)
        temp = []
        while True:
            for i in level:
                if isinstance(i, Nitelik):                                           #düğüm ise
                    for j in i.kenarlarim :                                         #kenarlarında gez
                        hdfnt = Nitelik(ism=hedefNitelikAdi, data=j.data)
                        genelentro = self.genelEntropiHesapla(hdfNit=hdfnt)
                        gain=0
                        node=None
                        toplam=0
                        for k in nitelikler:
                            x = Nitelik(ism=k, data=j.data, hdfNit=hdfnt)
                            agirlikliEntropi = self.agirlikliEntropiBul(nitelik=x)
                            toplam=toplam+agirlikliEntropi
                            if gain < self.kazancHesapla(genelEntropi=genelentro, NitEntropi=agirlikliEntropi):
                                gain = self.kazancHesapla(genelEntropi=genelentro, NitEntropi=agirlikliEntropi)
                                node = x

                        if toplam==0:
                            print(i.isim, "niteliğinin", j.isim, "kenarı için  in target node u :",j.data[hedefNitelikAdi][0])
                            j.targetNode = node
                            temp.append(node)
                        else:
                            print(i.isim, "niteliğinin", j.isim, "kenarı için  in target node u :", node.isim)
                            j.targetNode = node
                            temp.append(node)
                            nitelikler.remove(node.isim)
                else:
                    temp.append(i)



            dugumVarMı = False
            for i in temp:
                if isinstance(i, Nitelik):
                    dugumVarMı = True

            if dugumVarMı == False:                                  #düğüm yok ise ağaç oluştu demek
                break
            else:                                                   #düğüm var ise devam etmeliyiz.
                level.clear()
                level = temp.copy()
                temp.clear()




    def kokBul(self,nitelikListesi,genelEntropi):
        gain = 0
        rootNode = None
        for i in nitelikListesi:
            agirlikliEntropi = self.agirlikliEntropiBul(nitelik=i)
            if gain < self.kazancHesapla(genelEntropi=genelEntropi, NitEntropi=agirlikliEntropi):
                gain = self.kazancHesapla(genelEntropi=genelEntropi, NitEntropi=agirlikliEntropi)
                rootNode = i
        return gain,rootNode






















    """
    for i in root.kenarlarim:                                   #kökte gez
                                                                    #direk yaprağa bağlanıyorsa bağla bağlanmıyorsa "düğüm" değerini ata
            x = self.yaprakBul(kenar=i,hedefKolonunDegerleri=root.HedefKolonumunDegerleri,sinifinSayilari=i.sinifiminSayilariSozluk)
            level.append(x)
            #print("\nYaprak sa değeri değilse düğüm yaz :",x)
    
            newData = data[data[root.isim] == i.isim]               #root niteliğinin i kenarına göre veriyi filtreledim.
            newData = newData.reset_index(drop=True)
            print("\nNew Data : \n", newData)
            print("\nSözlük:",i.sinifiminSayilariSozluk)
    """