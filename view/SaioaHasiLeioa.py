import view.ZailtasunLeioa as za
import view.PasBerLeioa as pas
import view.EzabatuLeioa as eza
import tkinter as tk
from model.Erabiltzaileak import *
from PIL import ImageTk, Image

class SaioaHasi(object):

    def __init__(self, izena):
        super(SaioaHasi, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        self.erab1 = Erabiltzailea()

        # TETRIS LOGO
        self.img = ImageTk.PhotoImage(Image.open("logo.png").reduce(2))
        self.panel = tk.Label(self.window, image=self.img, bg="light blue")
        self.panel.pack(side="top", fill="both", expand="no")

        zerb = tk.Frame(self.window)
        zerb.config(width=880, height=520, bg="light blue")
        zerb.pack()

        # erab izena
        izena_ikusi="Izena: "+izena
        izena_et = tk.Label(zerb, text=izena_ikusi, bg="light blue")
        izena_et.grid(column=0, row=1)
        print(self.erab1.puntuazioaLortu(izena))
        punt_ikusi="Puntuazioa: "+self.erab1.puntuazioaLortu(izena)
        punt_et = tk.Label(zerb, text=punt_ikusi, bg="light blue")
        punt_et.grid(column=0, row=2)

        jokatu = tk.Button(zerb, text="Jokatu", command= self.zailtasunLeioaZabaldu)
        jokatu.grid(column=0, row=3)

        pa_ald = tk.Button(zerb, text="Pasahitza aldatu", command=lambda:self.pasahitzaLeioaZabaldu(izena))
        pa_ald.grid(column=0, row=4)

        if self.erab1.administratzaileaDa(izena):
            ezabatu = tk.Button(zerb, text="Erabiltzailea ezabatu", command=lambda:self.ezabatuLeioaZabaldu(izena))
            ezabatu.grid(column=0, row=5)


    def zailtasunLeioaZabaldu(self):
        self.window.destroy()
        za.ZailtasunLeioa()

    def pasahitzaLeioaZabaldu(self, izena):
        self.window.destroy()
        pas.PasBerLeioa(True, izena)

    def ezabatuLeioaZabaldu(self, izena):
        self.window.destroy()
        eza.EzabatuLeioa(izena)