#Gerekli Kütüphaneler
import pandas as pd
from Hesapla import MC_Karar_Agaci

#Veri import
dosya_adi = "PlayGolf.csv"
data = pd.read_csv(dosya_adi)


trainData = pd.DataFrame(data.iloc[0:9]) #train
testData = pd.DataFrame(data.iloc[8:14]) #test

#model oluştur.
MC = MC_Karar_Agaci()
hedefNitelikAdi = "Play Golf"
R = MC.modelOlustur(trainData, hedefNitelikAdi)

#Tahmin yap
print("\n")
sonuc = MC.tahminEt(root=R, test=testData,i=8)# i test verisinin kaçıncı indisten başladığı.
print("Tahmin sonucu :", sonuc)














