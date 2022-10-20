from model.Erabiltzaileak import *
from tkinter import messagebox
import tkinter as tk
import view.ErregistratuLeioa as er
import view.SaioaHasiLeioa as sa
import view.PasBerLeioa as pas
from PIL import ImageTk, Image

class HasierakoLeioa(object):

    def __init__(self):
        super(HasierakoLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        self.erab_izen = tk.StringVar()
        self.erab_pas = tk.StringVar()
        self.erab_gal1 = tk.StringVar()
        self.erab_gal2 = tk.StringVar()

        self.erab1 = Erabiltzailea()

        self.hasierakoOrria()
    def hasierakoOrria(self):
        # TETRIS LOGO
        self.img = ImageTk.PhotoImage(Image.open("logo.png").reduce(2))
        panel = tk.Label(self.window, image=self.img,  bg="light blue")
        panel.pack(side="top", fill="both", expand="no")
        # logoa = tk.PhotoImage(file='logo.png')
        # logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
        # log_img = tk.Label(self.window, image=logoa_sub)
        # log_img.pack()

        # Hasiera------------------------------LOGIN
        login=tk.Frame (self.window)
        login.pack()
        login.config(width=880, height=520, bg="light blue")

        # erab izena
        izena_et = tk.Label(login, text="Izena:", bg="light blue")
        izena_et.grid(column=0, row=1)
        pas_et = tk.Label(login, text="Pasahitza:", bg="light blue")
        pas_et.grid(column=0, row=3)

        # balioak hartu
        # erab_izen = tk.StringVar()
        # erab_pas = tk.StringVar()
        izen_sar = tk.Entry(login, textvariable=self.erab_izen)
        izen_sar.grid(column=0, row=2)
        pas_sar = tk.Entry(login, textvariable=self.erab_pas, show="*")
        pas_sar.grid(column=0, row=4)

        # onartu botoIA
        onartu_bot = tk.Button(login, text='Onartu', command= self.saioaHasi)
        onartu_bot.grid(column=0, row=5)
        # ez zaude erregistratuta?
        erreg_bot = tk.Button(login, text='Erregistratu',command=self.erregistratuLeioaZabaldu)
        pasahitza_et = tk.Button(login, text="Pasahitza ahaztu duzu?", command=self.pasahitzaLeioaZabaldu)
        erreg_bot.grid(column=0, row=6)
        # pasaahitza ahaztu duzu?
        pasahitza_et.grid(column=0, row=7)

        # button = tk.Button(self.window, text="Partida hasi")
        # button.pack()

        self.window.mainloop()

    def erregistratuLeioaZabaldu(self):
        self.window.destroy()
        print("rk")
        er.ErregistratuLeioa()
    #.erabBerria(onartu_bot, erreg_bot, pasahitza_et)

    def pasahitzaLeioaZabaldu (self):
        self.window.destroy()
        pas.PasBerLeioa(False)
       # self.pasahitzaBerresk(onartu_bot, erreg_bot, pasahitza_et, pas_sar, pas_et)

    def saioaHasi(self):
        # erab1 = Erabiltzailea()
        print("JOKATU LEIOA--> SAIOA HASI")
        hasi = self.erab1.saioa_hasi(self.erab_izen.get(), self.erab_pas.get())
        print(hasi)
        if hasi:
            em = messagebox.showinfo("Konektuta", "Saioa hasi da")
            self.window.destroy()
            sa.SaioaHasi(self.erab_izen.get())
        else:
            existitu = self.erab1.erab_badag(self.erab_izen.get())
            print("EXISTITU")
            print(existitu)
            if not existitu:
                em = messagebox.showerror("Errorea", "Izen horrekin ez dago erabiltzailerik")
                self.erab_izen.set("")
            else:
                aukeraGehiago = self.erab1.saiakera_badu()
                if aukeraGehiago:
                    em = messagebox.showerror("Errorea", "Pasahitza okerra, saiatu berriz")
                else:
                    em = messagebox.showerror("Errorea", "Saiakerak bukatu dira")
                    self.window.destroy()
            self.erab_pas.set("")

