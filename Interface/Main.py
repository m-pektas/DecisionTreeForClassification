from msilib import Table
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pandastable import Table,TableModel
import pandas as pd

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
    print("dosya yolu : ",file_path)

    dataset = pd.read_csv(file_path)

    
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


root.mainloop()


