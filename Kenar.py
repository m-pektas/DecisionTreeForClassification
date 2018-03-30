"Bu sınıf her bir niteliğin bir ayrık değerine yani kenarına denk gelmektedir."

class Kenar:
    def __init__(self,ism):
        self.isim=ism
        self.toplamSayim=0

    def sinifiminSayilariniAyarla(self,hedefDegerleriSayisi):
        self.sinifiminSayilari=[0]*hedefDegerleriSayisi