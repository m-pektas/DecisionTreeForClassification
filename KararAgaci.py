#Gerekli Kütüphaneler
import pandas as pd
from Nitelik import Nitelik



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

print(nitelikListesi[0].isim,"niteliginin", nitelikListesi[0].kenarlarim[0].isim, "kenarının farklı sınıf sayilari :",
      nitelikListesi[0].kenarlarim[0].sinifiminSayilari)
print(nitelikListesi[0].isim," niteliğinin ",nitelikListesi[0].kenarlarim[0].isim," kenarının toplam bulunma sayısı :",
      nitelikListesi[0].kenarlarim[0].toplamSayim)
















