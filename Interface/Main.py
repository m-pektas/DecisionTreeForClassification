from msilib import Table
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pandastable import Table,TableModel
import pandas as pd
from Hesapla import MC_Karar_Agaci


#gerekli değişkenler
test_sinir_indeks = 0


#pencere oluşturma
root = Tk()
root.title("Karar Ağacı Projesi")
root.geometry("1000x500")
#app = Frame(root)
#app.grid()

frame1 = Frame(root)
frame1.pack()


#label ekleme
label = Label(frame1,text="       Cevher ile Muhammed'in sınıflandırma için otomatik karar ağacı programına hoşgeldiniz..")
label.grid()


label3 = Label(frame1,text="                       ")
label3.grid(row= 3,column = 0)

def btn1Tıklandı():
    root2 = Tk()
    root2.withdraw()
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Csv Files", "*.csv"),("All files", "*.*")))

    global dataset
    dataset = pd.read_csv(file_path)

    frame2 = Frame(root)
    frame2.pack(side=BOTTOM)  # asagıda cerceve olusmasını sağladık.
    pt = Table(frame2, dataframe=dataset, showstatusbar=True, showtoolbar=True)
    pt.show()


def btn2Tıklandı():
    root3 = Tk()
    root3.title("Model - Başarı")
    root3.geometry("1000x500")

    test_sinir_indeks = int(entry2.get())
    trainData = dataset.iloc[0:test_sinir_indeks]  # train
    testData = dataset.iloc[test_sinir_indeks-1:dataset.shape[0]]  # test

    # model oluştur.
    MC = MC_Karar_Agaci()
    hedefNitelikAdi = entry1.get()

    R,model = MC.modelOlustur(trainData, hedefNitelikAdi)

    # Tahmin yap
    print("\n")
    sonuc = MC.tahminEt(root=R, test=testData, i=8)  # i test verisinin kaçıncı indisten başladığı.
    print("Tahmin sonucu :", sonuc)

    frame3 = Frame(root3)
    frame3.pack(side=LEFT)

    listbox = Listbox(frame3,width=50, height=50)
    for i in model:
        listbox.insert(END,i)
    listbox.pack(fill=BOTH, expand=0)

    frame4 = Frame(root3)
    frame4.pack(side=RIGHT)


    score=0
    index = 0
    for i in testData[hedefNitelikAdi]:
        if i == sonuc[index]:
            score = score +1

        index = index + 1


    accuracy_score =  score / len(testData[hedefNitelikAdi])
    print(accuracy_score)

    list = []
    for i in sonuc:
        list.append(i)

    list.append("")
    list.append("Accuracy Score : " + str(accuracy_score))

    listbox2 = Listbox(frame4,width=50, height=50)
    for i in list:
        listbox2.insert(END,i)
    listbox2.pack(fill=BOTH, expand=0)

    root3.mainloop()

btn1 = Button(frame1,text="Dataset seç",fg="blue" ,command=btn1Tıklandı)
btn1.grid(row=2)

label2 = Label(frame1,text="Hedef Kolonu Giriniz:")
label2.grid(row= 5,column = 0,sticky = E, pady=1)
entry1 = Entry(frame1)
entry1.grid(row=5, column = 1)



label3 = Label(frame1,text="Eğitim veriseti sınır indeksini yazınız:")
label3.grid(row= 6,column = 0,sticky = E, pady=1)
entry2 = Entry(frame1)
entry2.grid(row=6, column = 1)

btn2 = Button(frame1,text="Sonuçları Göster",fg="green" ,command=btn2Tıklandı)
btn2.grid(row=6)


root.mainloop()


