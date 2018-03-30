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
        self.kenarlariminHedefDegeriSayisi()  #kenarların hedeflerinin ayrık değer sayıları ayarlandı.
        if not self.HedefMi:
            self.kenarlarinSinifDegerleriniBul()



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
        if not self.HedefMi:
            for i in self.kenarlarim:
                i.sinifiminSayilariniAyarla(hedefDegerleriSayisi=len(self.HedefKolonumunDegerleri))


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

    def kenarlarinSinifDegerleriniBul(self):
        nitelikKolon=self.kolonHalim
        hedefKolon=self.HedefNiteligim.kolonHalim
        if(self.kenarlarim is None):
            print("***İlginç bir şekilde bu niteliğin kenarım listesi boş. Bu metod çalışamaz..")
        else:
            for i in range(0,len(nitelikKolon)):                                    #Niteliğimin değerlerinde gez
                for j in range(0,len(self.kenarlarim)):                             #kenarlarımda gez
                    if nitelikKolon[i]==self.kenarlarim[j].isim:                         #kenarlarımdan kaçıncıya denk geliyor ise
                        for k in range(0,len(self.HedefKolonumunDegerleri)):
                            if hedefKolon[i] == self.HedefKolonumunDegerleri[k]:
                                #hangi sınıftan kac tane oldugunu sayıyor.
                                self.kenarlarim[j].sinifiminSayilari[k] = self.kenarlarim[j].sinifiminSayilari[k]+1
                                #o kenarın kaç adet değeri oluğunu hesaplıyor.
                                self.kenarlarim[j].toplamSayim = self.kenarlarim[j].toplamSayim + 1