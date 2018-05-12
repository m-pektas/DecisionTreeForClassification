# Bu sınıf gerekli matematiksel hesaplamaların yapıldığı sınıftır.

from math import log2
from Nitelik import Nitelik


class MC_Karar_Agaci:

    # Verilen niteligin entropisinin ağırlıklı ortalamasını bulur
    def genelEntropiHesapla(self, hdfNit):
        degerlerSozlugu = hdfNit.kenarlariminSayilari                 #hedef niteliğin kenarlarının etiket sayısını al.
        toplamKayıtSayisi = len(hdfNit.kolonHalim)                    #toplam kayıt sayısı
        sonuc = 0

        for i in hdfNit.kenarlarim:                                   #kenarlarımda gez
            x = degerlerSozlugu[i.isim] / toplamKayıtSayisi           #kenarımın olasılığı
            sonuc = sonuc + ((-x) * log2(x))                          #kenarın entopisini bul her kenarın entropisini topla

        return sonuc                                                  #sonuc genel entropi dir sonucu döndür.

    #genel entropiden Niteliğin ağırlıklı entropisini çıkaran kazanç hesaplama fonksiyonu.
    def kazancHesapla(self, genelEntropi, NitEntropi):
        sonuc = genelEntropi - NitEntropi
        return sonuc

    #Her niteliğin kenarlarının entropilerini ağırlıklarıyla çarparak toplar. Ve niteliğin ağırlıklı entropisini döndürür.
    def agirlikliEntropiBul(self, nitelik):
        kenarlar = nitelik.kenarlarim                                       #niteliğin kenarları alındı.
        toplamKayitSayisi = len(nitelik.kolonHalim)                         #toplam kayıt sayısı bulundu
        hedefNiteliginAyrikDegerleri = nitelik.HedefKolonumunDegerleri      #sınıf etiketleri alındı.
        sonuc = 0
        for i in kenarlar:                                                  #kenarlarda gez
            for j in hedefNiteliginAyrikDegerleri:                          #sınıf etiketlerinde gez
                a = i.sinifiminSayilariSozluk[j]                            #etiket için o kenarda bulunma sayısını bul
                if a == 0:                                                  #eğer etiket hiç bulunmamışsa entropi 0
                    entropi = 0
                else:                                                       #eger etiketin 0 olduğu hiç bir kenar yoksa
                    s = i.toplamSayim                                       #kenarın eleman sayısı bulundu
                    r = a / s                                               #sınıf etiketinin olasılığı bulunudu
                    agirlik = s / toplamKayitSayisi                         #ağırlık hesaplandı
                    entropi = (-r) * log2(r)                                #entropi hesaplandı.

                sonuc = sonuc + (agirlik * entropi)  # her entropi ağırlığıyla çarpılıp toplanarak agırlıklı entropi hesaplandı.

        return sonuc                                 #butun değerler için işlem bittiğinde niteliğin ağırlıklı entropisi bulundu.

    # ağaç oluşturur.
    def CreateTree(self, root, hedefNitelikAdi, nitelikler):

        MODEL=[]
        print("---------------------------------------------")
        print("Oluşturulan Ağaç Yapısı :")
        print("---------------------------------------------")

        nitelikler.remove(root.isim)                          #her nitelik bir kere kullanılacağından kök nitelik listeden çıkarıldı.

        nitelik_bitti = False
        level = []                                            #level adında boş bir liste oluşturuldu.
        level.append(root)                                    #level nesnesine root eklendi
        temp = []                                             #temp adında bir değiş-tokuş listesi oluşturuldu.

        while True:
            for i in level:                                                #levelda gez
                if isinstance(i, Nitelik):  # düğüm ise                    #eleman nitelik ise
                    if i.isim == root.isim:                                #ve kök ise kök üğüm olarak adını yazdır
                        print("Kök Düğüm :" + i.isim)
                        MODEL.append(str("Kök Düğüm :" + i.isim))
                    else:                                                  #değil ise düğüm olarak yazdır
                        print("Düğüm :" + i.isim)
                        MODEL.append(str("Düğüm :" + i.isim))
                    for j in i.kenarlarim:                                 #niteliğin kenarlarında gez
                        hdfnt = Nitelik(ism=hedefNitelikAdi, data=j.data)  #kenarın filtelenmiş datasına göre hedef nit oluştur.
                        genelentro = self.genelEntropiHesapla(hdfNit=hdfnt)#genel entropiyi hesapla
                        gain = 0
                        node = None
                        toplam = 0
                        for k in nitelikler:                                        #kullanılmamış niteliklerde gez
                            x = Nitelik(ism=k, data=j.data, hdfNit=hdfnt)           #filtrelenmiş data ile yenilerini oluştur.
                            agirlikliEntropi = self.agirlikliEntropiBul(nitelik=x)  #agırlıklı entropisini hesapla
                            toplam = toplam + agirlikliEntropi                      #ağırlıklı entropiyi topla
                            if gain < self.kazancHesapla(genelEntropi=genelentro, NitEntropi=agirlikliEntropi): #en kazançlı olanının
                                gain = self.kazancHesapla(genelEntropi=genelentro, NitEntropi=agirlikliEntropi) #kazancını gain'e
                                node = x                                                                        #kendisini de node'a at


                        if toplam == 0:                                                                         #eğer gain 0 ise
                            print("\tKenar :", j.isim, " Leaf :", j.data[hedefNitelikAdi][0])                   #yaprağa ulaşıldı demek
                            item = str("Kenar :"+ str(j.isim) + " Leaf :"+ str(j.data[hedefNitelikAdi][0])+" ")
                            MODEL.append(item)
                            j.targetNode = j.data[hedefNitelikAdi][0]                                           #kenarın hedef node unu o yaprak yap
                            temp.append(node)                                                                   #temp e ekle
                        else:

                            if node is None:
                                print("<<< Nitelik  bitti.. >>>")
                                nitelik_bitti = True
                                break  # kenarlarım döngüsünden çıkar

                            print("\tKenar :", j.isim, " Child :", node.isim)                                   #düğüme ulaşıldı demek
                            MODEL.append(str("Kenar :"+ j.isim+ " Child :"+ node.isim))
                            j.targetNode = node                                                                 #hedef nodu u bulunan düğüm yap
                            temp.append(node)                                                                   #gecici listeye ekle
                            nitelikler.remove(node.isim)                                                        #ve kullanılabilir nitelikler listesinden çıkar.

                    if nitelik_bitti is True:
                        break

                else:                                    #nitelik değil ise direk temp e ekle.
                    temp.append(i)

            if nitelik_bitti is True:
                break

            #temp te hiç düğüm var  mı bak.
            dugumVarMı = False
            for i in temp:
                if isinstance(i, Nitelik):
                    dugumVarMı = True

            #yok ise tüm sonuçlar yaprağa ulaştı demek.
            if dugumVarMı == False:                     #düğüm yok ise ağaç oluştu demek
                break                                   #Ağaç ı sonlandır.
            else:                                       #düğüm var ise devam etmeliyiz.
                level.clear()                           #level listesini sil
                level = temp.copy()                     #temp i level e kopyala
                temp.clear()                            #temp i sil.

        print("-----------------------------------------")
        return root, MODEL                                      #oluşan ağacın kök ünü döndür.

    def kokBul(self, nitelikListesi, genelEntropi):      #tüm nüteliklerin entropisi bulur ve birini kök seçer.
        gain = 0
        rootNode = None
        for i in nitelikListesi:
            agirlikliEntropi = self.agirlikliEntropiBul(nitelik=i)
            if gain < self.kazancHesapla(genelEntropi=genelEntropi, NitEntropi=agirlikliEntropi):
                gain = self.kazancHesapla(genelEntropi=genelEntropi, NitEntropi=agirlikliEntropi)
                rootNode = i
        return gain, rootNode

    #aldığı ağaç modelinin kökü ve test verisiyle ağaçta gezinerek tahminler yapar
    def tahminEt(self, root, test, i):

        gecici = root
        index = i
        sınır = test.shape[0] + i
        result = []

        while index < sınır:
            gecici = root
            while True:
                for i in gecici.kenarlarim:
                    if test[gecici.isim][index] == i.isim:
                        gecici = i.targetNode
                        break

                if isinstance(gecici, str):
                    break

            result.append(gecici)
            index = index + 1

        return result

    #ağaç olşturme işlemlerinden ilk başta kökü seçmeye kadar model oluşturmak için her işi sırayla yaptıran metod.
    def modelOlustur(self, data, hedefNitelikAdi):

        # alınan data dan gerekli nitelikler oluşturuldu.

        nitelik_adlari = data.columns.values.tolist()
        nitelik_adlari.remove(hedefNitelikAdi)
        hedefNitelik = Nitelik(ism=hedefNitelikAdi, data=data)

        nitelikListesi = []
        for i in nitelik_adlari:
            x = Nitelik(ism=i, data=data, hdfNit=hedefNitelik)
            nitelikListesi.append(x)

        # kök düğümü oluştur.
        genelEntropi = self.genelEntropiHesapla(hdfNit=hedefNitelik)
        print("\t-Genel Entropi :", genelEntropi)
        gain, rootNode = self.kokBul(nitelikListesi=nitelikListesi, genelEntropi=genelEntropi)
        print("\t-Genel Entropi:", genelEntropi, " dir ve kök için en iyi node :", rootNode.isim,
              " olarak bulundu. Ve bu node un gaini :", gain)

        kok,model = self.CreateTree(root=rootNode, hedefNitelikAdi=hedefNitelikAdi, nitelikler=nitelik_adlari)

        return kok,model
