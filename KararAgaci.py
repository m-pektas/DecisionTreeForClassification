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


                                #---------Kök düğüm hesaplama----------
print("*** KÖK DÜĞÜM HESAPLAMA ***")

hm=HesapMakinesi()
genelEntropi = hm.genelEntropiHesapla(hdfNit=hedefNitelik)
print("\t-Genel Entropi :",genelEntropi)
gain,rootNode=hm.kokBul(nitelikListesi=nitelikListesi,genelEntropi=genelEntropi)
print("\t-Genel Entropi:",genelEntropi," dir ve kök için en iyi node :",rootNode.isim," olarak bulundu. Ve bu node un gaini :",gain)
print("*Kök düğüm hesaplama bitti.")
                                        #**Kök düğüm bulundu**

                             #------------Ağaç Oluştur-----------------

print("\n\n")
print("*** AĞAÇ OLUŞTUR ***")
hm.CreateTree(root=rootNode,hedefNitelikAdi=hedefNitelikAdi,nitelikler=nitelikler)









"""
print ("--------------------15.04.2018---------------------------")
xyz = data[data['Outlook']=='Sunny']
xyz = xyz.reset_index(drop=True)
xyzhedefNitelik=Nitelik(ism=hedefNitelikAdi,data=xyz)

print("Filtrelenmiş Veri : \n",xyz)
print("\nFiltrelenmiş Veri Genel Entropi :",hm.genelEntropiHesapla(hdfNit=xyzhedefNitelik))
newNitelik = Nitelik(ism='Temp',data=xyz,hdfNit=xyzhedefNitelik)
print("Filtrelenmiş Veride seçilen bir niteliğin ağırlıklı ortalaması : : ",hm.agirlikliEntropiBul(nitelik=newNitelik))
"""













