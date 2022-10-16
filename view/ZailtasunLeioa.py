from view.JokatuLeioa import JokatuLeioa
import tkinter as tk

class ZailtasunLeioa(object):

    def __init__(self):
        super(ZailtasunLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('300x460')
        self.window.title("Tetris jokoa")
        self.window.configure(bg='light blue')

        # TETRIS LOGO
        logoa = tk.PhotoImage(file='logo.png')
        logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
        log_img = tk.Label(self.window, image=logoa_sub)
        log_img.pack()

        # Zailtasun mailak agertu-----------------------------------------------
        zail_maila = tk.Frame(self.window)
        zail_maila.config(width=880, height=520, bg="light blue")
        erraza = tk.Button(zail_maila, text="Erraza", command=self.zailJok(200))
        erraza.place(width=80, height=80)
        # erraza.pack()
        erraza.grid(column=0, row=1)
        normala = tk.Button(zail_maila, text="Normala", command=self.zailJok(400))
        normala.place(width=70, height=140)
        #normala.grid(column=0, row=2)
        zaila = tk.Button(zail_maila, text="Zaila", command=self.zailJok(600))
        zaila.place(width=80, height=200)
        #normala.grid(column=0, row=3)
        # #normala.pack()
        # #zaila.pack()

    def zailJok(self, abiadura):
        tetris=JokatuLeioa(abiadura)