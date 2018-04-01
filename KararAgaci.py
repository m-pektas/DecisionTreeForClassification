#Gerekli Kütüphaneler
import pandas as pd
from Nitelik import Nitelik
from Hesapla import HesapMakinesi

#Veri import
dosya_adi="PlayGolf.csv"
data=pd.read_csv(dosya_adi)

#Nitelik isimleri
nitelikler=["Outlook","Temp","Humidity","Windy"] #data.columns diyerekte alınabilirdi
hedefNitelikAdi="Play Golf"
hedefNitelik=Nitelik(ism=hedefNitelikAdi,data=data)


#Her niteliği nesne yap
nitelikListesi=[]
for i in nitelikler:
    x=Nitelik(ism=i,data=data,hdfNit=hedefNitelik)
    nitelikListesi.append(x)


                                        #Kök düğüm hesaplama

#herhangi bir niteliğin kenarlarının sayısı ve hedef kolondaki hangi sınıfa kaç kere denk geldiği
for i in  nitelikListesi[0].kenarlarim:
    print("-",i.sinifiminSayilariSozluk)

print(nitelikListesi[0].isim," niteliğinin ",nitelikListesi[0].kenarlarim[0].isim," kenarının toplam bulunma sayısı :",
      nitelikListesi[0].kenarlarim[0].toplamSayim)

#hedef kolondaki ayrık değer ve sayılari.
print("---Hedef Nitelik---")
hm=HesapMakinesi()
genelEntropi = hm.genelEntropiHesapla(hdfNit=hedefNitelik)
print("Genel Entropi :",genelEntropi)


print("\nagırlıklı ortalama :",hm.agirlikliEntropiBul(nitelik=nitelikListesi[0]))














