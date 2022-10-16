from model.Erabiltzaileak import *
import tkinter as tk
from tkinter import messagebox
#from view.HasierakoLeioa import HasierakoLeioa

class PasBerLeioa(object):

    global erab_izen, erab_pas, erab1, erab_gal1, erab_gal2
    window = tk.Tk()

    erab_izen = tk.StringVar()
    erab_pas = tk.StringVar()
    erab_gal1 = tk.StringVar()
    erab_gal2 = tk.StringVar()


    erab1 = Erabiltzailea()

    def __init__(self):
        super(PasBerLeioa, self).__init__()
        # self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        # TETRIS LOGO
        logoa = tk.PhotoImage(file='logo.png')
        logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
        log_img = tk.Label(self.window, image=logoa_sub)
        log_img.pack()
        self.hasierakoOrria()

        datuak = tk.Frame(self.window)
        datuak.pack()
        datuak.config(width=880, height=520, bg="light blue")

        izena_et = tk.Label(datuak, text="Izena:")
        izena_et.grid(column=0, row=1)
        izen_sar = tk.Entry(datuak, textvariable=erab_izen)
        izen_sar.grid(column=0, row=2)

        galdera1_et = tk.Label(datuak, text="Zein da zure lehen animaliaren izena?")
        galdera1_et.grid(column=0, row=3)
        galdera2_et = tk.Label(datuak, text="Zure NAN-ren azken 2 digituak eta letra?")
        galdera2_et.grid(column=0, row=5)

        gal1_sar = tk.Entry(datuak, textvariable=erab_gal1)
        gal1_sar.grid(column=0, row=4)
        gal2_sar = tk.Entry(datuak, textvariable=erab_gal2)
        gal2_sar.grid(column=0, row=6)

        onartu_bot = tk.Button(datuak, text='Onartu', command=self.erantzunaZuzena)
        onartu_bot.grid(column=0, row=7)

    def pasahitzaBerresk(self, erreg_bot, onartu_bot, pasah_bot, pasah, pas_et):
        #erreg_bot.destroy()
        onartu_bot.destroy()
        pasah_bot.destroy()
        pasah.destroy()
        pas_et.destroy()
        self.galderak(False)

    def pasahitzaAld(self, datuak):
        datuak.destroy()
        pasahitzaBer = tk.Frame(self.window)
        pasahitzaBer.pack()
        pasahitzaBer.config(width=880, height=520, bg="light blue")
        pas_et = tk.Label(pasahitzaBer, text="Pasahitza:")
        pas_et.grid(column=0, row=1)
        pas_sar = tk.Entry(pasahitzaBer, textvariable=erab_pas, show="*")
        pas_sar.grid(column=0, row=2)
        print("PASAHITZA")
        print(erab_pas.get())
        # onartu botoIA
        print("BOTOIA")
        onartu_bot = tk.Button(pasahitzaBer, text='Onartu', command=lambda: self.hasierara_bueltatu(pasahitzaBer))
        onartu_bot.grid(column=0, row=3)

    def erantzunaZuzena(self, datuak):
        print(erab_izen.get())
        print(erab_gal1.get())
        print("PASAH ALD")
        zuzena = erab1.galderaZuzenak(erab_izen.get(), erab_gal1.get(), erab_gal2.get())
        if zuzena:
            #pasahitza sartzeko aukera
            self.pasahitzaAld(datuak)
        else:
            em = messagebox.showerror("Error", "Galdeeretako bat edo erabiltzailea ez da zuzena")

    def hasierara_bueltatu(self, pasahitza):
        print("HAS BUELT")
        if erab_pas.get() is not None:
            aldatu = erab1.pasahAld(erab_izen.get(), erab_pas.get())
            if aldatu:
               # pasahitza.destroy()
               # tetris= HasierakoLeioa()
                self.window.destroy()
                em = messagebox.showinfo("Pasahitza berreskuratu", "Pasahitza aldatu da")
        em=messagebox.showerror("Error","Pasahitza ezin da hutsa izan.")