import tkinter as tk
from tkinter import ttk
from tkinter import * 
import mysql.connector



veritab = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sirket"
    
)
print(veritab,"başarıyla veri tabanını bağlanıldı")

islem=veritab.cursor()

#islem.execute("CREATE DATABASE sirket")

#islem.execute("CREATE TABLE sirket (id INT AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(255), soyAd VARCHAR(255), dTarih VARCHAR(255), mail VARCHAR(255), dp VARCHAR(255), bolum VARCHAR(255), cinsiyet VARCHAR(255), egitim VARCHAR(255), maaş VARCHAR(255), deneyim VARCHAR(255))")

#DATABASE

def veriekle():
      sorgu ="INSERT INTO sirket (ad , soyAd, dTarih,mail,  egitim,  deneyim) VALUES (%s,%s,%s,%s,%s,%s)"
      deger =(ad.get(),
            soyad.get(),
            dTarihi.get(),
            mail.get(),
            #departmanlar.get(),
            #bolumler.get(),
            listBoxOne.get(ACTIVE),
            #maas.get(),
            listBoxTwo.get(ACTIVE))
      islem.execute(sorgu,deger)
      veritab.commit()


root = Tk()

def calıstır(event):
  if departmanlar.get()=="WEB":
    bolumler['values']=webbolum
  if departmanlar.get()=="Grafik":
    bolumler['values']=grafikbolum
  if departmanlar.get()=="Sosyal Medya":
    bolumler['values']=sosyalmedyabolum
  if departmanlar.get()=="İçerik":
    bolumler['values']=icerikbolum
  if departmanlar.get()=="Kreatif":
    bolumler['values']=kreatifbolum

# This is the section of code which creates the main window
root.geometry('888x1500')
root.configure(background='#76EEC6')
root.title('RFN AJANS')
rfndepartman=['WEB', 
            'Grafik', 
            'Sosyal Medya', 
            'İçerik', 
            'Kreatif']

# This is the section of code which creates a combo box
departmanlar= ttk.Combobox(root, 
                          values=rfndepartman, 
                          font=('arial', 14, 'normal'), 
                          width=12)
departmanlar.bind('<<ComboboxSelected>>', calıstır)
departmanlar.place(x=140, y=190)
departmanlar.current(0)


webbolum=['Google Reklam', 
            'SEO', 
            'Yazılım', 
            'Tasarım', 
            'Güncelleme']

grafikbolum=['Fotoğrafçı', 
             'Grafiker']

sosyalmedyabolum=['Hesap Yöneticisi', 
                  'Grafiker']

icerikbolum=['Metin Yazarı', 
             'Tasarım']

kreatifbolum=['Sunum', 
              'Müşteri Temsilci']

# This is the section of code which creates a combo box
bolumler= ttk.Combobox(root, 
                      values=webbolum, 
                      font=('arial', 14, 'normal'), 
                      width=15)
bolumler.place(x=140, y=220)
bolumler.current(0)


# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return departmanlar.get()


# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return bolumler.get()

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = ad.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = soyad.get()
	return userInput


# This is the section of code which creates the a label
Label(root, 
      text='Adınız', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=70)

# This is the section of code which creates a text input box
ad=Entry(root)
ad.pack()
ad.place(x=140, y=70)



# This is the section of code which creates the a label
Label(root, 
      text='Soyadınız', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=100)

Label(root, 
      text='Doğum Tarihi', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=130)

# this is a function which returns the selected spin box value
def getSelectedSpinBoxValue():
	return dTarihi.get()

# This is the section of code which creates a spin box
dTarihi= Spinbox(root, 
                  from_=1950, 
                  to=2000, 
                  font=('arial', 12, 'normal'), 
                  bg = '#F0F8FF', 
                  width=6)
dTarihi.place(x=140, y=130)




# This is the section of code which creates a text input box
soyad=Entry(root)
soyad.place(x=140, y=100)


def btnOnclicked():
      veriekle()
      print("Veritabanına verileriniz başarıyla eklendi")
      Label(root, 
            text=ad.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=70)      
      Label(root, 
            text=soyad.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=100)
      Label(root, 
            text=dTarihi.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=130)
      Label(root, 
            text=mail.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=160)
      Label(root, 
            text=departmanlar.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=190)
      Label(root, 
            text=bolumler.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=220)
      Label(root, 
            text="ERKEK", 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=250)
      Label(root, 
            text=listBoxOne.get(ACTIVE), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=310)
      Label(root, 
            text=maas.get(), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=370)
      Label(root, 
            text=listBoxTwo.get(ACTIVE), 
            bg='#F0F8FF', 
            font=('arial', 12, 'normal')).place(x=370, y=430)

	

# This is the section of code which creates a button
Button(root, 
        text='KAYDET', 
        bg='#CD3333', 
        font=('arial', 15, 'normal'), 
        command=btnOnclicked).place(x=200, y=500),


        

# This is the section of code which creates a text input box
mail=Entry(root)
mail.place(x=140, y=160)


# This is the section of code which creates the a label
Label(root, 
      text='Mail adresiniz', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=160)



Label(root, 
      text='Departman', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=190)


Label(root, 
      text='Cinsiyet', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=250)

Label(root, 
      text='Bölüm', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=220)

Label(root, 
      text='Eğitim', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=299)




frame=IntVar()

# This is the section of code which creates a group of radio buttons
frame=Frame(root, width=0, height=0, bg='#F0F8FF')
frame.place(x=140, y=250)

Radiobutton(frame, text="Erkek", variable=frame, value=1,bg='#F0F8FF', font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')
Radiobutton(frame, text="Kadın", variable=frame, value=2,bg='#F0F8FF', font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')
  

# This is the section of code which creates a listbox
listBoxOne=Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
listBoxOne.insert('0', 'Lise')
listBoxOne.insert('1', 'Önlisans')
listBoxOne.insert('2', 'Lisans')
listBoxOne.insert('3', 'Yüksek Lisans')
listBoxOne.place(x=140, y=280)

Label(root, 
      text='Maaş', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=370)

maas=Entry(root)
maas.place(x=140, y=370)

Label(root, 
      text='Deneyim', 
      bg='#F0F8FF', 
      font=('arial', 12, 'normal')).place(x=10, y=420)

listBoxTwo=Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'),width=5, height=4)
listBoxTwo.insert('0', '0-1')
listBoxTwo.insert('1', '1-2')
listBoxTwo.insert('2', '2-5')
listBoxTwo.insert('3', '10+')
listBoxTwo.place(x=140, y=400,)


























root.mainloop()
