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
root.geometry("1480x800")

frame1 = Frame(root)
frame1.pack()


#label ekleme
title = Label(frame1,text="\n Cevher ile Muhammed'in sınıflandırma için otomatik karar ağacı programına hoşgeldiniz..\n\n",font=16,fg="purple")
title.grid()


def Load():
    root2 = Tk()
    root2.withdraw()
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("All files", "*.*"),("Csv Files", "*.csv"),("Data Files", "*.data")))

    global dataset
    dataset = pd.read_csv(file_path)

    frame2 = Frame(root)
    frame2.pack(side=BOTTOM)  # asagıda cerceve olusmasını sağladık.
    pt = Table(frame2, dataframe=dataset, showstatusbar=True, showtoolbar=True,width=1000,height=500)
    pt.show()


def getResult():
    root3 = Tk()
    root3.title("Model - Başarı")
    root3.geometry("1480x800")

    test_sinir_indeks = int(trainingLimitEntry.get())
    trainData = dataset.iloc[0:test_sinir_indeks]  # train
    testData = dataset.iloc[test_sinir_indeks:dataset.shape[0]+1]  # test

    # model oluştur.
    MC = MC_Karar_Agaci()
    hedefNitelikAdi = targetColumnEntry.get()

    R,model = MC.modelOlustur(trainData, hedefNitelikAdi)

    # Tahmin yap
    print("\n")
    sonuc = MC.tahminEt(root=R, test=testData, i=test_sinir_indeks)  # i test verisinin kaçıncı indisten başladığı.
    print("Tahmin sonucu :", sonuc)

    frame3 = Frame(root3)
    frame3.pack(side=LEFT)

    listbox = Listbox(frame3,width=50, height=50,font=16)
    for i in model:
        listbox.insert(END,i)
    listbox.pack(fill=BOTH, expand=0)

    frame4 = Frame(root3)
    frame4.pack(side=RIGHT)


    score=0
    index = 0
    for i in testData[hedefNitelikAdi]:
        if i == sonuc[index]:
            score = score + 1

        if len(sonuc)-1 == index:
            break

        index = index + 1



    accuracy_score =  score / len(testData[hedefNitelikAdi])
    print(accuracy_score)
    list = []

    list.append("Sonuçlar")
    list.append("Accuracy Score : " + str(accuracy_score))
    list.append("")
    list.append("")
    for i in range(len(sonuc)):
        list.append("P:" + str(sonuc[i])+" T:" + str(testData.iloc[i][hedefNitelikAdi]))

    listbox2 = Listbox(frame4, width=50, height=50,font=16)
    for i in list:
        listbox2.insert(END, i)
    listbox2.pack(fill=BOTH, expand=0)

    root3.mainloop()


LoadDatasetBtn = Button(frame1, text=" Dataset seç ", fg="blue", command=Load,font=16)
LoadDatasetBtn.grid(row=2)

spacerLabel = Label(frame1,text=" ")
spacerLabel.grid(row=3, column=0, sticky=W, pady=1)

targetColumnLabel = Label(frame1,text="Hedef Kolonu Giriniz: \n",font=14)
targetColumnLabel.grid(row=4, column=0, sticky=W, pady=1)
targetColumnEntry = Entry(frame1,font=14)
targetColumnEntry.grid(row=4, column=0,sticky=N)

maxDeptLabel = Label(frame1,text="*iptal* Maksimum Derinlik: \n",font=14)
maxDeptLabel.grid(row=5, column=0, sticky=W)
maxDeptEntry = Entry(frame1,font=14)
maxDeptEntry.grid(row=5,column=0,sticky=N)

trainingLimitLabel = Label(frame1,text="Eğitim veriseti sınır indeksi:\n",font=14)
trainingLimitLabel.grid(row=6, column=0, sticky=W)
trainingLimitEntry = Entry(frame1,font=14)
trainingLimitEntry.grid(row=6, column = 0,sticky=N)

getResultBtn = Button(frame1,text="Sonuçları Göster",fg="green" ,command=getResult,font=16)
getResultBtn.grid(row=7)


root.mainloop()


