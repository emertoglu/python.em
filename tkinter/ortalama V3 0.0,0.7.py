#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from Tkinter import *


pencere = Tk()
pencere.title("ortalama")
pencere.geometry("160x400+500+100")
pencere.resizable(width=FALSE,height=FALSE)

#hakkinda
def hakkinda():
    hakkinda= Tk()
    hakkinda.title("Hakkında")
    hakkinda.geometry("160x180+500+190")
    hakkinda.resizable(width=FALSE,height=FALSE)
    Label(hakkinda,text=
          "*SIRADIŞI*\ncorporation\n\nortalama\nV3 0.0,0.7\n\nLisans:\ntabiki özgür\n" ,
          fg="#660000" ).pack()
    url=Label(hakkinda,text="websites\nkil.bil.omu.edu.tr",fg="#660000")
    url.pack()
    def tikla(env=None):
        webbrowser.open('http://kil.bil.omu.edu.tr')
    def ust(env=None):
        url["fg"] = "darkblue"
    def terket(env=None):
        url["fg"]="#660000"
    url.bind("<Button-1>",tikla)
    url.bind("<Enter>",ust)
    url.bind("<Leave>",terket)
Button( text="hakkında" , fg="#660000" ,width=16,height=1,
    command = hakkinda).grid(row=19,column=0,columnspan=3)
    
def hesapla():
    k=0
    t=0
    if ekran1.get() !="":
        i=ekran1.get()
        j=ekran13.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran2.get() !="":
        i=ekran2.get()
        j=ekran14.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran3.get() !="":
        i=ekran3.get()
        j=ekran15.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran4.get() !="":
        i=ekran4.get()
        j=ekran16.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran5.get() !="":
        i=ekran5.get()
        j=ekran17.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran6.get() !="":
        i=ekran6.get()
        j=ekran18.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran7.get() !="":
        i=ekran7.get()
        j=ekran19.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran8.get() !="":
        i=ekran8.get()
        j=ekran20.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran9.get() !="":
        i=ekran9.get()
        j=ekran21.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran10.get() !="":
        i=ekran10.get()
        j=ekran22.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran11.get() !="":
        i=ekran11.get()
        j=ekran23.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i
    if ekran12.get() !="":
        i=ekran12.get()
        j=ekran24.get()
        i=float(i)
        j=float(j)
        k=k+i
        if 0<=j<30:
            j=0
        if 30<=j<40:
            j=0.5
        if 40<=j<50:
            j=1
        if 50<=j<60:
            j=1.5
        if 60<=j<68:
            j=2
        if 68<=j<76:
            j=2.5
        if 76<=j<84:
            j=3
        if 84<=j<92:
            j=3.5
        if 92<=j<=100:
            j=4
        i=(i*j)
        t=t+i


    i=t/k
    ortalama.delete(0,END)
    ortalama.insert(END,i)

#Butonlar
Button( text="hesapla" , fg="#660000" ,width=7,height=1,
        command = hesapla).grid(row=15,column=1,columnspan=2)

#Ekranlar
ortalama = Entry(width=6)
ortalama.grid(row=17, column=2, columnspan=1)

ekran1 = Entry(width=6)
ekran1.grid(row=3, column=1, columnspan=1)
ekran2 = Entry(width=6)
ekran2.grid(row=4, column=1, columnspan=1)
ekran3 = Entry(width=6)
ekran3.grid(row=5, column=1, columnspan=1)
ekran4 = Entry(width=6)
ekran4.grid(row=6, column=1, columnspan=1)
ekran5 = Entry(width=6)
ekran5.grid(row=7, column=1, columnspan=1)
ekran6 = Entry(width=6)
ekran6.grid(row=8, column=1, columnspan=1)
ekran7 = Entry(width=6)
ekran7.grid(row=9, column=1, columnspan=1)
ekran8 = Entry(width=6)
ekran8.grid(row=10, column=1, columnspan=1)
ekran9 = Entry(width=6)
ekran9.grid(row=11, column=1, columnspan=1)
ekran10 = Entry(width=6)
ekran10.grid(row=12, column=1, columnspan=1)
ekran11 = Entry(width=6)
ekran11.grid(row=13, column=1, columnspan=1)
ekran12 = Entry(width=6)
ekran12.grid(row=14, column=1, columnspan=1)

ekran13 = Entry(width=6)
ekran13.grid(row=3, column=2, columnspan=1)
ekran14 = Entry(width=6)
ekran14.grid(row=4, column=2, columnspan=1)
ekran15 = Entry(width=6)
ekran15.grid(row=5, column=2, columnspan=1)
ekran16 = Entry(width=6)
ekran16.grid(row=6, column=2, columnspan=1)
ekran17 = Entry(width=6)
ekran17.grid(row=7, column=2, columnspan=1)
ekran18 = Entry(width=6)
ekran18.grid(row=8, column=2, columnspan=1)
ekran19 = Entry(width=6)
ekran19.grid(row=9, column=2, columnspan=1)
ekran20 = Entry(width=6)
ekran20.grid(row=10, column=2, columnspan=1)
ekran21 = Entry(width=6)
ekran21.grid(row=11, column=2, columnspan=1)
ekran22 = Entry(width=6)
ekran22.grid(row=12, column=2, columnspan=1)
ekran23 = Entry(width=6)
ekran23.grid(row=13, column=2, columnspan=1)
ekran24 = Entry(width=6)
ekran24.grid(row=14, column=2, columnspan=1)

#Label
Label(text="" , fg="#660000").grid(row=16 , column=1,columnspan=2,ipady=2)
Label(text="" , fg="#660000").grid(row=18 , column=1,columnspan=2,ipady=2)
Label(text="Ortalamanız:" , fg="#660000").grid(row=17 , column=0,columnspan=2)

Label(text="Kredi" , fg="#660000").grid(row=2 , column=1)
Label(text="ortalama" , fg="#660000").grid(row=2 , column=2)

Label(text="1.ders" , fg="#660000").grid(row=3 , column=0)
Label(text="2.ders" , fg="#660000").grid(row=4 , column=0)
Label(text="3.ders" , fg="#660000").grid(row=5 , column=0)
Label(text="4.ders" , fg="#660000").grid(row=6 , column=0)
Label(text="5.ders" , fg="#660000").grid(row=7 , column=0)
Label(text="6.ders" , fg="#660000").grid(row=8 , column=0)
Label(text="7.ders" , fg="#660000").grid(row=9 , column=0)
Label(text="8.ders" , fg="#660000").grid(row=10 , column=0)
Label(text="9.ders" , fg="#660000").grid(row=11 , column=0)
Label(text="10.ders" , fg="#660000").grid(row=12 , column=0)
Label(text="11.ders" , fg="#660000").grid(row=13 , column=0)
Label(text="12.ders" , fg="#660000").grid(row=14 , column=0)

mainloop()
