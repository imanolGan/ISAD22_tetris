import tkinter as tk
from model.Erabiltzaileak import *
from PIL import ImageTk, Image
from tkinter import messagebox
import view.SaioaHasiLeioa as sa

class EzabatuLeioa(object):

    def __init__(self, izena):
        super(EzabatuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        self.erab1 = Erabiltzailea()

        # TETRIS LOGO
        self.img = ImageTk.PhotoImage(Image.open("logo.png").reduce(2))
        panel = tk.Label(self.window, image=self.img,  bg="light blue")
        panel.pack(side="top", fill="both", expand="no")

        self.eguneratuZerrenda(izena)

    def eguneratuZerrenda(self, izena):
        ezab = tk.Frame(self.window)
        ezab.pack()
        ezab.config(width=880, height=520, bg="light blue")

        erabiltzaileZerrenda= self.erab1.erabiltzaileakEtaPuntuazioakLortu()

        i=0
        for key, value in erabiltzaileZerrenda.items():
            print("SORTU")
            print(key)
            i+=1
            print(i)
            print(value)
            et=f"Izena:{key} --> puntuazioa:{str(value)}"
            print(et)
            zerrenda_et = tk.Label(ezab, text=et, bg="light blue")
            zerrenda_et.grid(column=0, row=i)

        i+=1
        izena_et=tk.Label(ezab, text="Erabiltzaile izena sartu:", bg="light blue" )
        izena_et.grid(column=0, row= i)

        i += 1
        self.erab_izen = tk.StringVar()
        izen_sar = tk.Entry(ezab, textvariable=self.erab_izen)
        izen_sar.grid(column=0, row=i)

        i+=1
        onartu_bot = tk.Button(ezab, text='Onartu', command=lambda: self.erabEzabatu(self.erab_izen.get(), izena,ezab ))
        onartu_bot.grid(column=0, row=i)

    def erabEzabatu(self, erabEzabizena, erabIzena, ezab):
        print(erabEzabizena)
        if erabEzabizena==erabIzena:
            messagebox.showerror("ERROR","Zeure burua ezin duzu ezabatu")
            self.erab_izen.set("")
        else:
            if self.erab1.erab_badag(erabEzabizena):
                self.erab1.ezabatu(erabEzabizena)
                messagebox.showinfo("EZABATUTA","Erabiltzailea ezabatu da")
                gal_admi = messagebox.askyesno(message="Erabiltzaile gehiago ezabatu nahi duzu?", title="Ezabatu aukera")
                print(gal_admi)
                if gal_admi:
                    self.erab_izen.set("")
                    ezab.destroy()
                    self.eguneratuZerrenda(erabIzena)
                else:
                    self.window.destroy()
                    sa.SaioaHasi(erabIzena)
            else:
                messagebox.showerror("Errorea","Izen horrekin erabiltzailerik ez dago")
                self.erab_izen.set("")
