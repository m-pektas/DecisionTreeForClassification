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

hm=HesapMakinesi()
genelEntropi = hm.genelEntropiHesapla(hdfNit=hedefNitelik)
print("Genel Entropi :",genelEntropi)

gain=0
rootNode=None
for i in nitelikListesi:
    agirlikliEntropi=hm.agirlikliEntropiBul(nitelik=i)
    if gain < hm.kazancHesapla(genelEntropi=genelEntropi,NitEntropi=agirlikliEntropi):
        gain = hm.kazancHesapla(genelEntropi=genelEntropi,NitEntropi=agirlikliEntropi)
        rootNode=i

print("Genel Entropi:",genelEntropi," dir ve kök için en iyi node :",rootNode.isim," olarak bulundu. Ve bu node un gaini :",gain)


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

print("------------------16.04.2018--------------------------")
#print("RootNode :",[i.isim for i in rootNode.kenarlarim])
hm.CreateTree(root=rootNode,data=data)
















