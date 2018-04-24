#Bu sınıf  bir niteliğin bir kenarına denk gelmektedir.

class Kenar:

    def __init__(self, ism, data):
        self.isim = ism                     #kenarın ismi
        self.toplamSayim = 0                #bu ayrık değerin o nitelikte kaç adet bulunduğu
        self.sinifiminSayilariSozluk = {}   #bu ayrık değere hangi sınıftan kaç etiket denk geldiği
        self.targetNode = None              #niteliğin bu kenarının bağlandığı Nitelik yada Leaf
        self.data = data                    #kenara ait filtrelenmis data

