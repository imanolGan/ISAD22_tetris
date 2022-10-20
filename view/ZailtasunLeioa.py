import view.JokatuLeioa as jok
import tkinter as tk
from PIL import ImageTk, Image

class ZailtasunLeioa(object):

    def __init__(self):
        super(ZailtasunLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        # TETRIS LOGO
        img = ImageTk.PhotoImage(Image.open("logo.png").reduce(2))
        panel = tk.Label(self.window, image=img, bg="light blue")
        panel.pack(side="top", fill="both", expand="no")
       # logoa = tk.PhotoImage(file='logo.png')
        #logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
        #log_img = tk.Label(self.window, image=logoa_sub)
        #log_img.pack()

        # Zailtasun mailak agertu-----------------------------------------------
        zail_maila = tk.Frame(self.window)
        zail_maila.config(width=880, height=520, bg="light blue")
        zail_maila.pack()

        erraza = tk.Button(zail_maila, text="Erraza", command=lambda :self.zailJok(200))
        erraza.place(width=80, height=80)
        erraza.pack()
        #erraza.grid(column=0, row=1)
        normala = tk.Button(zail_maila, text="Normala", command=lambda :self.zailJok(400))
        normala.place(width=80, height=140)
        #normala.grid(column=0, row=2)
        zaila = tk.Button(zail_maila, text="Zaila", command=lambda :self.zailJok(600))
        zaila.place(width=80, height=200)
        #normala.grid(column=0, row=3)
        normala.pack()
        zaila.pack()

        self.window.mainloop()

    def zailJok(self, abiadura):
        self.window.destroy()
        tamaina=[]
        if abiadura==200:
            tamaina.append(15)
            tamaina.append(30)
        if abiadura==400:
            tamaina.append(10)
            tamaina.append(25)
        else:
            tamaina.append(10)
            tamaina.append(20)
        jok.JokatuLeioa(abiadura, tamaina)