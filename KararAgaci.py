#Gerekli Kütüphaneler
import pandas as pd
from Nitelik import Nitelik



#Veri import
dosya_adi="PlayGolf.csv"
data=pd.read_csv(dosya_adi)
print(data.head())

#Nitelik isimleri
nitelikler=["Outlook","Temp","Humidity","Windy"] #data.columns diyerekte alınabilirdi
hedefNitelikAdi="Play Golf"
hedefNitelik=Nitelik(ism=hedefNitelikAdi,data=data)


#Her niteliği nesne yap
nitelikListesi=[]
for i in nitelikler:
    x=Nitelik(ism=i,data=data)
    nitelikListesi.append(x)


#Kök düğüm hesaplama
















