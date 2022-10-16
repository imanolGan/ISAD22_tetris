from model.Erabiltzaileak import *
from tkinter import messagebox
import tkinter as tk

class ErregistratuLeioa(object):
    global erab_izen, erab_pas, erab1, erab_gal1, erab_gal2, signOn, login, canvas, zail_maila
    window = tk.Tk()

    erab_izen = tk.StringVar()
    erab_pas = tk.StringVar()
    erab_gal1 = tk.StringVar()
    erab_gal2 = tk.StringVar()

    signOn = tk.Frame(window)

    erab1 = Erabiltzailea()
    def __init__(self):
        super(ErregistratuLeioa, self).__init__()
        # self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        # TETRIS LOGO
        logoa = tk.PhotoImage(file='logo.png')
        logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
        log_img = tk.Label(self.window, image=logoa_sub)
        log_img.pack()

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

    def erabGehitu(self):
        print(erab_izen.get())
        print(erab_gal1.get())
        print("ERABGEHITU")
        if erab_izen.get():
            if erab1.erab_badag(erab_izen.get()):
                em = messagebox.showerror("Error", "Izen horrekin jada dago erabiltzailea")
                erab_izen.set('')
            else:
                erab1.erab_gehitu(erab_izen.get(), erab_pas.get(), erab_gal1.get(), erab_gal2.get())
                # if sortuta:
                em = messagebox.showinfo("SORTUTA", "Erabiltzaile berri gehitu da")
                signOn.destroy()
                onartu_bot = tk.Button(login, text='Onartu', command=self.saioaHasi)
                onartu_bot.grid(column=0, row=5)
                erreg_bot = tk.Button(login, text='Erregistratu')
                erreg_bot.config(command=lambda: self.erabBerria(onartu_bot, erreg_bot))
                erreg_bot.grid(column=0, row=6)
            # else: TODO: ID 2 zenbaki eta letra bat direla frogatu
        else:
            em = messagebox.showerror("Error", "Daturen bat utsik")

    def erabBerria(self, onartu_bot, erreg_bot, pasah_bot):
        erreg_bot.destroy()
        onartu_bot.destroy()
        pasah_bot.destroy()

        # self.window.destroy()
        # self.erabSortzekoWindow = tk.Tk().Toplevel(self.window)
        # self.erabSortzekoWindow.geometry('300x460')
        # self.erabSortzekoWindow.title("Tetris jokoa")
        # self.erabSortzekoWindow.configure(bg='light blue')
        # signOn=tk.Frame(self.window)
        self.galderak(True)

    def galderak(self, erabGehitzen):
        signOn.pack()
        signOn.config(width=880, height=520, bg="light blue")
        # erab izena
        # izena_et = tk.Label(signOn, text="Izena:")
        # izena_et.grid(column=0, row=1)
        # pas_et = tk.Label(signOn, text="Pasahitza:")
        # pas_et.grid(column=0, row=3)
        galdera1_et = tk.Label(signOn, text="Zein da zure lehen animaliaren izena?")
        galdera1_et.grid(column=0, row=5)
        galdera2_et = tk.Label(signOn, text="Zure NAN-ren azken 2 digituak eta letra?")
        galdera2_et.grid(column=0, row=7)

        # balioak hartu
        # erab_izen = tk.StringVar()
        # erab_pas = tk.StringVar()
        # izen_sar = tk.Entry(signOn, textvariable=erab_izen)
        # izen_sar.grid(column=0, row=2)
        # pas_sar = tk.Entry(signOn, textvariable=erab_pas, show="*")
        # pas_sar.grid(column=0, row=4)
        gal1_sar = tk.Entry(signOn, textvariable=erab_gal1)
        gal1_sar.grid(column=0, row=6)
        gal2_sar = tk.Entry(signOn, textvariable=erab_gal2)
        gal2_sar.grid(column=0, row=8)

        # onartu botoIA
        if erabGehitzen:
            onartu_bot = tk.Button(signOn, text='Onartu', command=self.erabGehitu)
            onartu_bot.grid(column=0, row=9)
        else:
            onartu_bot = tk.Button(signOn, text='Onartu', command=self.pasahitzaZuzena)
            onartu_bot.grid(column=0, row=9)
        self.window.mainloop()
