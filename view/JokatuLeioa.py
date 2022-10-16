import random
import tkinter as tk
from model.Tableroa import Tableroa
from model.Piezak import *
from model.Erabiltzaileak import *
from tkinter import messagebox

class JokatuLeioa(object):
	"""docstring for JokatuLeioa"""
	global erab_izen, erab_pas, erab1, erab_gal1, erab_gal2, signOn, login, canvas, zail_maila
	window=tk.Tk()

	erab_izen = tk.StringVar()
	erab_pas = tk.StringVar()
	erab_gal1 = tk.StringVar()
	erab_gal2 = tk.StringVar()

	login=tk.Frame(window)
	signOn = tk.Frame(window)
	zail_maila = tk.Frame(window)

	erab1 = Erabiltzailea()

	def __init__(self):
		super(JokatuLeioa, self).__init__()
		#self.window = tk.Tk()
		self.window.geometry('300x460')
		self.window.title("Tetris jokoa")
		self.window.configure(bg='light blue')


		# TETRIS LOGO
		logoa = tk.PhotoImage(file='logo.png')
		logoa_sub = logoa.subsample(2)  # dimentsioak txikitu
		log_img = tk.Label(self.window, image=logoa_sub)
		log_img.pack()
		self.hasierakoOrria()

	def hasierakoOrria(self):
		#Hasiera------------------------------LOGIN
		#login=tk.Frame (self.window)
		login.pack()
		login.config(width=880, height=520,bg="light blue" )

		#erab izena
		izena_et= tk.Label(login, text="Izena:")
		izena_et.grid(column=0,row=1)
		pas_et = tk.Label(login, text="Pasahitza:")
		pas_et.grid(column=0, row=3)

		#balioak hartu
		#erab_izen = tk.StringVar()
		#erab_pas = tk.StringVar()
		izen_sar= tk.Entry(login, textvariable=erab_izen)
		izen_sar.grid(column=0, row=2)
		pas_sar=tk.Entry(login, textvariable=erab_pas, show="*")
		pas_sar.grid(column=0, row=4)

		#onartu botoIA
		onartu_bot= tk.Button(login, text='Onartu', command=self.saioaHasi)
		onartu_bot.grid(column=0 , row=5)
		#ez zaude erregistratuta?
		erreg_bot=tk.Button(login, text='Erregistratu')
		pasahitza_et=tk.Button(login,text="Pasahitza ahaztu duzu?")
		erreg_bot.config( command=lambda: self.erabBerria(onartu_bot,erreg_bot, pasahitza_et))
		erreg_bot.grid (column=0, row=6)
		#pasaahitza ahaztu duzu?
		pasahitza_et.config( command=lambda: self.pasahitzaBerresk(onartu_bot,erreg_bot, pasahitza_et, pas_sar, pas_et))
		pasahitza_et.grid(column=0, row=7)


		#button = tk.Button(self.window, text="Partida hasi")
		#button.pack()

		self.window.mainloop()

	def erabBerria(self, onartu_bot,erreg_bot, pasah_bot):
		erreg_bot.destroy()
		onartu_bot.destroy()
		pasah_bot.destroy()

		#self.window.destroy()
		#self.erabSortzekoWindow = tk.Tk().Toplevel(self.window)
		#self.erabSortzekoWindow.geometry('300x460')
		#self.erabSortzekoWindow.title("Tetris jokoa")
		#self.erabSortzekoWindow.configure(bg='light blue')
		#signOn=tk.Frame(self.window)
		self.galderak(True)

	def galderak(self, erabGehitzen):
		signOn.pack()
		signOn.config(width=880, height=520,bg="light blue" )
		# erab izena
		#izena_et = tk.Label(signOn, text="Izena:")
		#izena_et.grid(column=0, row=1)
		#pas_et = tk.Label(signOn, text="Pasahitza:")
		#pas_et.grid(column=0, row=3)
		galdera1_et = tk.Label(signOn, text= "Zein da zure lehen animaliaren izena?")
		galdera1_et.grid(column=0, row=5)
		galdera2_et = tk.Label(signOn,text="Zure NAN-ren azken 2 digituak eta letra?")
		galdera2_et.grid(column=0, row=7)

		# balioak hartu
		# erab_izen = tk.StringVar()
		# erab_pas = tk.StringVar()
		#izen_sar = tk.Entry(signOn, textvariable=erab_izen)
		#izen_sar.grid(column=0, row=2)
		#pas_sar = tk.Entry(signOn, textvariable=erab_pas, show="*")
		#pas_sar.grid(column=0, row=4)
		gal1_sar=tk.Entry(signOn, textvariable=erab_gal1)
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
	def erabGehitu (self):
		print(erab_izen.get())
		print(erab_gal1.get())
		print("ERABGEHITU")
		if erab_izen.get() :
			if erab1.erab_badag(erab_izen.get()):
				em= messagebox.showerror("Error","Izen horrekin jada dago erabiltzailea")
				erab_izen.set('')
			else:
				erab1.erab_gehitu(erab_izen.get(), erab_pas.get(), erab_gal1.get(), erab_gal2.get())
				#if sortuta:
				em=messagebox.showinfo("SORTUTA","Erabiltzaile berri gehitu da")
				signOn.destroy()
				onartu_bot = tk.Button(login, text='Onartu', command=self.saioaHasi)
				onartu_bot.grid(column=0, row=5)
				erreg_bot = tk.Button(login, text='Erregistratu')
				erreg_bot.config(command=lambda: self.erabBerria(onartu_bot, erreg_bot))
				erreg_bot.grid(column=0, row=6)
				#else: TODO: ID 2 zenbaki eta letra bat direla frogatu
		else:
			em = messagebox.showerror("Error", "Daturen bat utsik")

	def saioaHasi(self):
		#erab1 = Erabiltzailea()
		print("JOKATU LEIOA--> SAIOA HASI")
		hasi=erab1.saioa_hasi(erab_izen.get(), erab_pas.get())
		print(hasi)
		if hasi:
			em=messagebox.showinfo("Konektuta","Saioa hasi da")
			self.zail_aukeratu()
		else:
			existitu=erab1.erab_badag(erab_izen.get())
			print("EXISTITU")
			print(existitu)
			if not existitu:
				em=messagebox.showerror("Errorea","Izen horrekin ez dago erabiltzailerik")
				erab_izen.set("")
			else:
				aukeraGehiago=erab1.saiakera_badu()
				if aukeraGehiago:
					em=messagebox.showerror("Errorea","Pasahitza okerra, saiatu berriz")
				else:
					em = messagebox.showerror("Errorea", "Saiakerak bukatu dira")
					self.window.destroy()
			erab_pas.set("")
	def pasahitzaBerresk(self, erreg_bot, onartu_bot, pasah_bot, pasah, pas_et):
		erreg_bot.destroy()
		onartu_bot.destroy()
		pasah_bot.destroy()
		pasah.destroy()
		pas_et.destroy()
		self.galderak(False)
	def pasahitzaAld(self, signOn,login):
		signOn.destroy()
		login.pack_forget()
		pasahitzaBer= tk.Frame(self.window)
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


	def pasahitzaZuzena(self):
		print(erab_izen.get())
		print(erab_gal1.get())
		print("PASAH ALD")
		zuzena=erab1.galderaZuzenak(erab_izen.get(),erab_gal1.get(),erab_gal2.get())
		if zuzena:
			self.pasahitzaAld(signOn,login )
		else:
			em=messagebox.showerror("Error","Galdeeretako bat edo erabiltzailea ez da zuzena")
	def hasierara_bueltatu(self, pasahitza):
		print("HAS BUELT")
		if erab_pas.get() is not None:
			aldatu=erab1.pasahAld(erab_izen.get(),erab_pas.get())
			if aldatu :
				pasahitza.destroy()
				self.hasierakoOrria()
				em = messagebox.showinfo("Pasahitza berreskuratu", "Pasahitza aldatu da")
	def zail_aukeratu(self):
		login.destroy()
		# Zailtasun mailak agertu-----------------------------------------------
		#zail_maila = tk.Frame(self.window)
		zail_maila.config(width=880, height=520, bg="light blue")
		erraza = tk.Button(zail_maila, text="Erraza", command=self.zailJok(200))
		# erraza.place(width=80, height=80)
		erraza.grid(column=0, row=1)
		normala = tk.Button(zail_maila, text="Normala", command=self.zailJok(400))
		#normala.place(width=70, height=140)
		normala.grid(column=0, row=2)
		zaila = tk.Button(zail_maila, text="Zaila", command=self.zailJok(600))
		#zaila.place(width=80, height=200)
		normala.grid(column=0, row=3)

		erraza.pack()
		normala.pack()
		zaila.pack()

	def zailJok(self, abiadura):
		zail_maila.destroy()
		# ---------------------------------BEHIN SARTUTRA
		puntuazioa = tk.StringVar()
		puntuazioa.set("Puntuazioa: 0")

		identif = tk.Frame(self.window)

		puntuazioalabel = tk.Label(identif, textvariable=puntuazioa)
		puntuazioalabel.pack()

		canvas = TableroaPanela(master=self.window, puntuazioalabel=puntuazioa)
		canvas.jolastu( abiadura)
		canvas.pack()
		self.window.bind("<Up>", canvas.joku_kontrola)
		self.window.bind("<Down>", canvas.joku_kontrola)
		self.window.bind("<Right>", canvas.joku_kontrola)
		self.window.bind("<Left>", canvas.joku_kontrola)

class TableroaPanela(tk.Frame):
	def __init__(self, tamaina=(10,20), gelazka_tamaina=20,puntuazioalabel=None, master=None):
		tk.Frame.__init__(self, master)
		self.puntuazio_panela = puntuazioalabel
		self.tamaina = tamaina
		self.gelazka_tamaina = gelazka_tamaina

		self.canvas = tk.Canvas(
			width=self.tamaina[0]  * self.gelazka_tamaina+1,
			height=self.tamaina[1] * self.gelazka_tamaina+1,
			bg='#eee', borderwidth=0, highlightthickness=0
		)
		self.canvas.pack(expand=tk.YES, fill=None)

		self.tab = Tableroa()
		self.jokatzen = None
		self.tableroa_ezabatu()


	def marratu_gelazka(self, x,y,color):
		self.canvas.create_rectangle(x*self.gelazka_tamaina, y*self.gelazka_tamaina,
									(x+1)*self.gelazka_tamaina, (y+1)*self.gelazka_tamaina, fill=color)

	def tableroa_ezabatu(self):
		self.canvas.delete("all")
		self.canvas.create_rectangle(0, 0, self.tamaina[0] * self.gelazka_tamaina, self.tamaina[1] * self.gelazka_tamaina, fill='#eee')

	def marraztu_tableroa(self):
		self.tableroa_ezabatu()
		for i in range(self.tab.tamaina[1]):
			for j in range(self.tab.tamaina[0]):
				if self.tab.tab[i][j]:
					self.marratu_gelazka(j,i,self.tab.tab[i][j])
		if self.tab.pieza:
			for i in range(4):
				x = self.tab.posizioa[0] + self.tab.pieza.get_x(i)
				y = self.tab.posizioa[1] + self.tab.pieza.get_y(i)
				self.marratu_gelazka(y,x,self.tab.pieza.get_kolorea())
		self.puntuazioa_eguneratu()


	def pausu_bat(self):
		try:
			self.tab.betetako_lerroak_ezabatu()
			self.tab.mugitu_behera()
		except Exception as error:
			try:
				self.tab.pieza_finkotu(self.tab.posizioa)
				pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
				self.tab.sartu_pieza(random.choice(pieza_posibleak)())
			except Exception as e:
				print("GAMEOVER")
				self.tab.hasieratu_tableroa()
				return
		self.after(400, self.pausu_bat)
		self.marraztu_tableroa()

	def puntuazioa_eguneratu(self):
		if self.puntuazio_panela:
			self.puntuazio_panela.set(f"Puntuazioa: {self.tab.puntuazioa}")

		

	def joku_kontrola(self, event):
		try:
			if event.keysym == 'Up':
				self.tab.biratu_pieza()
			if event.keysym == 'Down':
				self.tab.pieza_kokatu_behean()
			if event.keysym == 'Right':
				self.tab.mugitu_eskumara()
			if event.keysym == 'Left':
				self.tab.mugitu_ezkerrera()
		except Exception as error:
			pass
		finally:
			self.marraztu_tableroa()

	def jolastu(self, abiadura):
		if self.jokatzen:
			self.after_cancel(self.jokatzen)
		self.tab.hasieratu_tableroa()
		pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
		self.tab.sartu_pieza(random.choice(pieza_posibleak)())
		self.marraztu_tableroa()
		self.jokatzen = self.after(abiadura, self.pausu_bat)
		
	def erraza_jok(self):
		print("Maila erraza")
		self.jolastu(200)

	def normala_jok(self):
		print("Maila normala")
		self.jolastu(400)

	def zaila_jok(self):
		print("Maila zaila")
		self.jolastu(600)
