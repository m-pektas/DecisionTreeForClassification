#Bu nitelik sınıfı karar ağacındaki her bir düğümü temsil etmektedir.


from Kenar import Kenar

class Nitelik:
    #Nitelik oluşturulurken ismi,bulunduğu data yapısı tutulur,
    #ayrıca kenarlarının ne olduğu bilgiside hemen hesaplanarak muhafaza edilir.
    def __init__(self,ism,data):
        self.isim=ism
        self.data=data
        self.kolonHalim = data[ism]
        self.kenarlarim=self.KenarlarımıBul()


    #Bulunduğu niteliğin kenarlarını bulur birer nesne haline getirir ve döndürür
    #***Test Edildi***
    def KenarlarımıBul(self):
        kenarIsmleri=self.ayrıkDegerBul()
        kenarlar=[]
        for i in kenarIsmleri:
            x=Kenar(ism=i)
            kenarlar.append(x)
        return kenarlar


    #verilen datanın içinde verilen isimli kolondaki ayrık değerleri bulur ve liste hakinde döndürür.
    #***Test Edildi***
    def ayrıkDegerBul(self):
        kolon=self.kolonHalim
        ayrıkDegerler=[]
        for i in kolon:
            if i not in ayrıkDegerler:
                ayrıkDegerler.append(i)
        return ayrıkDegerler

    def kenarlarinSinifDegerleriniBul(self,hedefNitelik):
        nitelikKolon=self.kolonHalim
        hedefKolon=hedefNitelik.kolonHalim
        if(self.kenarlarim is None):
            print("***İlginç bir şekilde bu niteliğin kenarım listesi boş. Bu metod çalışamaz..")
        else:
            print("\n\n #kenarlarinSinifDegerleriniBul çalışıyorr..")
            for i in range(0,len(nitelikKolon)):
                for j in range(0,nitelikKolon.kenarlarim):
                    if nitelikKolon[i]==nitelikKolon.kenarlarim[j]:
                        nitelikKolon.kenarlarim[j].




