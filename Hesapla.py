
#Bu sınıf gerekli matematiksel hesaplamaların yapıldığı sınıftır.

from math import log2
from Nitelik import Nitelik

class MC_Karar_Agaci:

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


   #ağaç oluşturur.
    def CreateTree(self,root,hedefNitelikAdi,nitelikler):

        print("---------------------------------------------")
        print("Oluşturulan Ağaç Yapısı :")
        print("---------------------------------------------")

        nitelikler.remove(root.isim)

        level = []
        level.append(root)
        temp = []

        while True:
            for i in level:
                if isinstance(i, Nitelik):                                           #düğüm ise
                    if i.isim==root.isim:
                        print("Kök Düğüm :"+i.isim)
                    else:
                        print("Düğüm :" + i.isim)
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

                        if toplam == 0:
                            print("\tKenar :",j.isim," Leaf :", j.data[hedefNitelikAdi][0])
                            j.targetNode = j.data[hedefNitelikAdi][0]
                            temp.append(node)
                        else:
                            print("\tKenar :",j.isim," Child :", node.isim)
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

        print("-----------------------------------------")
        return root


    def kokBul(self,nitelikListesi,genelEntropi):
        gain = 0
        rootNode = None
        for i in nitelikListesi:
            agirlikliEntropi = self.agirlikliEntropiBul(nitelik=i)
            if gain < self.kazancHesapla(genelEntropi=genelEntropi, NitEntropi=agirlikliEntropi):
                gain = self.kazancHesapla(genelEntropi=genelEntropi, NitEntropi=agirlikliEntropi)
                rootNode = i
        return gain,rootNode


    def tahminEt(self,root,test,i):

        gecici = root
        index = i
        sınır = test.shape[0]+i
        result = []

        while index < sınır:
            gecici = root
            while True:
                for i in gecici.kenarlarim:
                    if test[gecici.isim][index] == i.isim:
                         gecici = i.targetNode
                         break

                if (isinstance(gecici, str)):
                    break

            result.append(gecici)
            index = index+1

        return result


    def modelOlustur(self,data,hedefNitelikAdi):

        #alınan data dan gerekli nitelikler oluşturuldu.

        nitelik_adlari = data.columns.values.tolist()
        nitelik_adlari.remove(hedefNitelikAdi)
        hedefNitelik = Nitelik(ism=hedefNitelikAdi, data=data)

        nitelikListesi = []
        for i in nitelik_adlari:
            x = Nitelik(ism=i, data=data, hdfNit=hedefNitelik)
            nitelikListesi.append(x)

        #kök düğümü oluştur.
        genelEntropi = self.genelEntropiHesapla(hdfNit=hedefNitelik)
        print("\t-Genel Entropi :", genelEntropi)
        gain, rootNode = self.kokBul(nitelikListesi=nitelikListesi, genelEntropi=genelEntropi)
        print("\t-Genel Entropi:", genelEntropi, " dir ve kök için en iyi node :", rootNode.isim,
              " olarak bulundu. Ve bu node un gaini :", gain)

        kok = self.CreateTree(root=rootNode, hedefNitelikAdi=hedefNitelikAdi, nitelikler=nitelik_adlari)

        return kok