#Bu nitelik sınıfı karar ağacındaki her bir düğümü temsil etmektedir.


from Kenar import Kenar


class Nitelik:

    #Nitelik oluşturulurken ismi,bulunduğu data yapısı tutulur,
    #ayrıca kenarlarının ne olduğu bilgiside hemen hesaplanarak muhafaza edilir.
    #Not: hedef niteliğin none olması hedef niteliğinin hedefi olmamasından kaynaklanır.Bu hedef nit e baglı olarak çalışan
    #ayrıkDegerBul metodu da buna uygun olarak hedef nit none ise kendi ayrık değerlerini hesaplıyor. :)
    def __init__(self,ism,data,hdfNit=None):
        self.HedefMi = False
        if hdfNit is None:
            self.HedefMi = True

        self.isim=ism
        self.data=data
        self.kolonHalim = data[ism]
        self.kenarlarim=self.KenarlarımıBul()
        self.HedefNiteligim=hdfNit
        self.HedefKolonumunDegerleri = self.ayrıkDegerBul(nit='hedef', Hedef=hdfNit)
        if not self.HedefMi:
            self.kenarlariminHedefDegeriSayisi()
        else:
            self.kenarlariminSayilari = self.kenarlariminSayilariniBul()
        self.kazanc = 0



    #Bulunduğu niteliğin kenarlarını bulur birer nesne haline getirir ve döndürür
    #***Test Edildi***
    def KenarlarımıBul(self):
        kenarIsmleri=self.ayrıkDegerBul()
        kenarlar=[]
        for i in kenarIsmleri:
            x=Kenar(ism=i)
            kenarlar.append(x)
        return kenarlar


    def kenarlariminHedefDegeriSayisi(self):
        dict = {}
        for l in self.kenarlarim:
            for i in self.HedefKolonumunDegerleri:
                l.sinifiminSayilariSozluk[i] = 0

        if not self.HedefMi:
            for i in range(0,len(self.kolonHalim)):
                for j in self.kenarlarim:
                    if self.kolonHalim[i] == j.isim:
                        j.toplamSayim = j.toplamSayim + 1
                        j.sinifiminSayilariSozluk[self.HedefNiteligim.kolonHalim[i]]=j.sinifiminSayilariSozluk[self.HedefNiteligim.kolonHalim[i]]+1


    #verilen datanın içinde verilen isimli kolondaki ayrık değerleri bulur ve liste hakinde döndürür.
    #***Test Edildi***
    def ayrıkDegerBul(self,nit='ben',Hedef=None):
        if nit=='ben' and Hedef is None:                     #Buralardaki şart ifadeleri verilen parametrelerin doğru
            kolon = self.kolonHalim                         #olup olmadığını kontrol eder.
        elif nit=='hedef' and Hedef is not None:             #yanlış ise metod None döndürür.
            kolon=Hedef.kolonHalim
        else:
            print("*Bilgi* Hedef kolonun hedef değerleri hesaplandı yada"
                  " Ayrık değer bul metoduna yanlış parametreler verildi.. ")
            return None

        ayrıkDegerler=[]
        for i in kolon:
            if i not in ayrıkDegerler:
                ayrıkDegerler.append(i)
        return ayrıkDegerler

    def kenarlariminSayilariniBul(self):
        dict={}                                 #her kenara karşılık sayac tululacak sözlük
        ayrikDegerlerim = self.ayrıkDegerBul()  #ayrık değerler bulundu

        for k in ayrikDegerlerim:               #her ayrık değerin başlangıç sayac değeri 0 yapildi
            dict[k]=0

        for i in range(0,len(self.kolonHalim)):  #kolonda gez
            for j in ayrikDegerlerim:            #ayrık değerlerde gez
                if self.kolonHalim[i] == j:      #kolondaki değer ayrık değerlerimden birine eşitse ki eşit olmak zorunda
                    dict[j]=dict[j]+1            #sözlükteki o ayrık değerin sayacını bir artır

        return dict

