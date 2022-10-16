from view.JokatuLeioa import JokatuLeioa
from model.Erabiltzaileak import Erabiltzailea
import view.db

if __name__ == '__main__':
	tetris = JokatuLeioa()
	view.db.ezabatuErab('Miri')
	#view.db.createTable()
#	view.db.erabGehitu('Maria','1234','erantzun1','erantzun2')
#	view.db.erabGehitu('Miriam', 'Aa1234', 'erantzun1', 'erantzun2')
	#erab1= Erabiltzailea('Maria','1234')