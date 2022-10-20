from model.Erabiltzaileak import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import view.HasierakoLeioa as has

#from tkinter.messagebox import askyesno

class ErregistratuLeioa(object):

    def __init__(self):
        super(ErregistratuLeioa, self).__init__()
        print("erreg")
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        self.erab1 = Erabiltzailea()

        # TETRIS LOGO
        self.img = ImageTk.PhotoImage(Image.open("logo.png").reduce(2))
        panel = tk.Label(self.window, image=self.img, bg="light blue")
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
        self.erab_izen = tk.StringVar()
        self.erab_pas = tk.StringVar()
        self.erab_gal1 = tk.StringVar()
        self.erab_gal2 = tk.StringVar()

        izen_sar = tk.Entry(login, textvariable=self.erab_izen)
        izen_sar.grid(column=0, row=2)
        pas_sar = tk.Entry(login, textvariable=self.erab_pas, show="*")
        pas_sar.grid(column=0, row=4)

        galdera1_et = tk.Label(login, text="Zein da zure lehen animaliaren izena?", bg="light blue")
        galdera1_et.grid(column=0, row=5)
        galdera2_et = tk.Label(login, text="Zure NAN-ren azken 2 digituak eta letra?", bg="light blue")
        galdera2_et.grid(column=0, row=7)

        gal1_sar = tk.Entry(login, textvariable=self.erab_gal1)
        gal1_sar.grid(column=0, row=6)
        gal2_sar = tk.Entry(login, textvariable=self.erab_gal2)
        gal2_sar.grid(column=0, row=8)

        # onartu botoIA
        onartu_bot = tk.Button(login, text='Onartu', command=self.erabGehitu)
        onartu_bot.grid(column=0, row=9)

        self.window.mainloop()

    def erabGehitu(self):
        print(self.erab_izen.get())
        print(self.erab_gal1.get())
        print("ERABGEHITU")
        if self.erab_izen.get():
            if self.erab1.erab_badag(self.erab_izen.get()):
                em = messagebox.showerror("Error", "Izen horrekin jada dago erabiltzailea")
                self.erab_izen.set('')
            else:
                gal_admi =messagebox.askyesno(message="Administratzailea zara?", title="Administratzailea")
                print(gal_admi)
                self.erab1.erab_gehitu(self.erab_izen.get(), self.erab_pas.get(), self.erab_gal1.get(), self.erab_gal2.get(), gal_admi)
                # if sortuta:
                #if gal_admi:
                 #   self.erab1.administratzaileBilakatu()
                em = messagebox.showinfo("SORTUTA", "Erabiltzaile berri gehitu da")
                self.window.destroy()
                has.HasierakoLeioa()
            # else: TODO: ID 2 zenbaki eta letra bat direla frogatu
        else:
            em = messagebox.showerror("Error", "Daturen bat utsik")



