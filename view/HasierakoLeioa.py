from model.Erabiltzaileak import *
from tkinter import messagebox
import tkinter as tk
from view.ErregistratuLeioa import ErregistratuLeioa
from view.ZailtasunLeioa import ZailtasunLeioa
from view.PasBerLeioa import PasBerLeioa

class HasierakoLeioa(object):
    global erab_izen, erab_pas, erab1, erab_gal1, erab_gal2, login
    window = tk.Tk()

    erab_izen = tk.StringVar()
    erab_pas = tk.StringVar()
    erab_gal1 = tk.StringVar()
    erab_gal2 = tk.StringVar()

    login = tk.Frame(window)

    erab1 = Erabiltzailea()

    def __init__(self):
        super(HasierakoLeioa, self).__init__()
        # self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        # TETRIS LOGO
        #logoa = tk.PhotoImage(file='logo.png')
        #logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
        #log_img = tk.Label(self.window, image=logoa_sub)
        #log_img.pack()
        self.hasierakoOrria()

    def hasierakoOrria(self):
        # Hasiera------------------------------LOGIN
        # login=tk.Frame (self.window)
        login.pack()
        login.config(width=880, height=520, bg="light blue")

        # erab izena
        izena_et = tk.Label(login, text="Izena:")
        izena_et.grid(column=0, row=1)
        pas_et = tk.Label(login, text="Pasahitza:")
        pas_et.grid(column=0, row=3)

        # balioak hartu
        # erab_izen = tk.StringVar()
        # erab_pas = tk.StringVar()
        izen_sar = tk.Entry(login, textvariable=erab_izen)
        izen_sar.grid(column=0, row=2)
        pas_sar = tk.Entry(login, textvariable=erab_pas, show="*")
        pas_sar.grid(column=0, row=4)

        # onartu botoIA
        onartu_bot = tk.Button(login, text='Onartu', command= self.saioaHasi)
        onartu_bot.grid(column=0, row=5)
        # ez zaude erregistratuta?
        erreg_bot = tk.Button(login, text='Erregistratu',command=lambda: self.erregistratuLeioaZabaldu )
        pasahitza_et = tk.Button(login, text="Pasahitza ahaztu duzu?", command=lambda: self.pasahitzaLeioaZabaldu)
        erreg_bot.grid(column=0, row=6)
        # pasaahitza ahaztu duzu?
        pasahitza_et.grid(column=0, row=7)

        # button = tk.Button(self.window, text="Partida hasi")
        # button.pack()

        self.window.mainloop()

    def erregistratuLeioaZabaldu(self):
        tetris= ErregistratuLeioa()
    #.erabBerria(onartu_bot, erreg_bot, pasahitza_et)

    def pasahitzaLeioaZabaldu (self):
        tetris=PasBerLeioa()
       # self.pasahitzaBerresk(onartu_bot, erreg_bot, pasahitza_et, pas_sar, pas_et)

    def saioaHasi(self):
        # erab1 = Erabiltzailea()
        print("JOKATU LEIOA--> SAIOA HASI")
        hasi = erab1.saioa_hasi(erab_izen.get(), erab_pas.get())
        print(hasi)
        if hasi:
            em = messagebox.showinfo("Konektuta", "Saioa hasi da")
            tetris = ZailtasunLeioa()
        else:
            existitu = erab1.erab_badag(erab_izen.get())
            print("EXISTITU")
            print(existitu)
            if not existitu:
                em = messagebox.showerror("Errorea", "Izen horrekin ez dago erabiltzailerik")
                erab_izen.set("")
            else:
                aukeraGehiago = erab1.saiakera_badu()
                if aukeraGehiago:
                    em = messagebox.showerror("Errorea", "Pasahitza okerra, saiatu berriz")
                else:
                    em = messagebox.showerror("Errorea", "Saiakerak bukatu dira")
                    self.window.destroy()
            erab_pas.set("")

