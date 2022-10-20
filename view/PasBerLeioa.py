from model.Erabiltzaileak import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import view.HasierakoLeioa as has
import view.SaioaHasiLeioa as sa
#from view.HasierakoLeioa import HasierakoLeioa

class PasBerLeioa(object):

    def __init__(self, saioaHasi, izena):
        super(PasBerLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        self.erab_izen = tk.StringVar()
        self.erab_pas = tk.StringVar()
        self.erab_gal1 = tk.StringVar()
        self.erab_gal2 = tk.StringVar()

        self.erab1 = Erabiltzailea()

        # TETRIS LOGO
        self.img = ImageTk.PhotoImage(Image.open("logo.png").reduce(2))
        panel = tk.Label(self.window, image=self.img, bg="light blue")
        panel.pack(side="top", fill="both", expand="no")

        datuak = tk.Frame(self.window)
        datuak.pack()
        datuak.config(width=880, height=520, bg="light blue")

        if not saioaHasi:
            izena_et = tk.Label(datuak, text="Izena:", bg="light blue")
            izena_et.grid(column=0, row=1)
            izen_sar = tk.Entry(datuak, textvariable=self.erab_izen)
            izen_sar.grid(column=0, row=2)

        galdera1_et = tk.Label(datuak, text="Zein da zure lehen animaliaren izena?", bg="light blue")
        galdera1_et.grid(column=0, row=3)
        galdera2_et = tk.Label(datuak, text="Zure NAN-ren azken 2 digituak eta letra?", bg="light blue")
        galdera2_et.grid(column=0, row=5)

        gal1_sar = tk.Entry(datuak, textvariable=self.erab_gal1)
        gal1_sar.grid(column=0, row=4)
        gal2_sar = tk.Entry(datuak, textvariable=self.erab_gal2)
        gal2_sar.grid(column=0, row=6)

        onartu_bot = tk.Button(datuak, text='Onartu', command=lambda:self.erantzunaZuzena(datuak, saioaHasi, izena))
        onartu_bot.grid(column=0, row=7)

    def pasahitzaBerresk(self, erreg_bot, onartu_bot, pasah_bot, pasah, pas_et):
        #erreg_bot.destroy()
        onartu_bot.destroy()
        pasah_bot.destroy()
        pasah.destroy()
        pas_et.destroy()
        self.galderak(False)

    def pasahitzaAld(self, datuak, saioaHasi, izena):
        datuak.destroy()
        pasahitzaBer = tk.Frame(self.window)
        pasahitzaBer.pack()
        pasahitzaBer.config(width=880, height=520, bg="light blue")
        pas_et = tk.Label(pasahitzaBer, text="Pasahitza:", bg="light blue")
        pas_et.grid(column=0, row=1)
        pas_sar = tk.Entry(pasahitzaBer, textvariable=self.erab_pas, show="*")
        pas_sar.grid(column=0, row=2)
        print("PASAHITZA")
        print(self.erab_pas.get())

        if not saioaHasi:
            self.izena_erab= self.erab_izen.get()
            print(self.erab_izen.get())
        else:
            self.izena_erab= izena

        # onartu botoIA
        print("BOTOIA")
        print(self.izena_erab)
        onartu_bot = tk.Button(pasahitzaBer, text='Onartu', command=lambda: self.hasierara_bueltatu(saioaHasi, self.izena_erab))
        onartu_bot.grid(column=0, row=3)

    def erantzunaZuzena(self, datuak, saioaHasi, izena):
        print(self.erab_gal1.get())
        print("PASAH ALD")
        zuzena = self.erab1.galderaZuzenak(izena, self.erab_gal1.get(), self.erab_gal2.get())
        if zuzena:
            #pasahitza sartzeko aukera
            self.pasahitzaAld(datuak, saioaHasi, izena)
        else:
            em = messagebox.showerror("Error", "Galdeeretako bat edo erabiltzailea ez da zuzena")

    def hasierara_bueltatu(self, saioaHasi, izena):
        print("HAS BUELT")
        if self.erab_pas.get() is not None:
            aldatu = self.erab1.pasahAld(self.erab_izen.get(), self.erab_pas.get())
            if aldatu:
               # pasahitza.destroy()
               # tetris= HasierakoLeioa()
                em = messagebox.showinfo("Pasahitza berreskuratu", "Pasahitza aldatu da")
                self.window.destroy()
                if saioaHasi:
                    sa.SaioaHasi(izena)
                else:
                    has.HasierakoLeioa()
        else:
            em=messagebox.showerror("Error","Pasahitza ezin da hutsa izan.")