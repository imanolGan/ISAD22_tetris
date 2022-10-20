import sqlite3

def createTable():
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS erabiltzailea("
            "izena text PRIMARY KEY, puntuazioa integer,"
            "pasahitza text NOT NULL, galdera1 text NOT NULL, "
            "galdera2 text NOT NULL, administratzailea boolean)")
    con.commit()
    con.close()

def erabGehitu (izena, pasahitza, gald1, gald2):
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    erag=f"INSERT INTO erabiltzailea VALUES ('{izena}',0,'{pasahitza}','{gald1}','{gald2}', False)"
    cur.execute(erag)
    con.commit()
    ema=erab_badago(izena)
    con.close()

def administratzaileBilakatu (erab):
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    erag =  ag = f" UPDATE erabiltzailea SET administratzailea=True WHERE izena='{erab}'"
    cur.execute(erag)
    con.commit()
    ema = erab_badago(erab)
    con.close()
    return ema

def erab_gald_lortu(erab,zenb):
    print(erab)
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag = f"SELECT galdera{zenb} FROM erabiltzailea WHERE izena='{erab}'"
    print(ag)
    res = cur.execute(ag)
    emaitza = res.fetchone()
    print(emaitza)
    con.commit()
    con.close()
    return emaitza

def erab_pasahitza_lortu(erab):
    print(erab)
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag=f"SELECT pasahitza FROM erabiltzailea WHERE izena='{erab}'"
    res = cur.execute(ag)
    emaitza=res.fetchone()
    print(emaitza)
    con.commit()
    con.close()
    return emaitza

def erab_zerrenda():
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    hashMap={}
    for res in cur.execute("SELECT izena, puntuazioa FROM erabiltzailea"):
        print(res)
        ema = str(res)
        print(ema)
        parentesiak = ema[2:len(ema) - 1]
        print(parentesiak)
        erab = parentesiak.split("',")
        print("LISTA")
        hashMap[erab[0]]=erab[1]
    print(hashMap)
    print("ZERRENDA")
    con.commit()
    con.close()
    return hashMap

def zenbatErab():
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag = "SELECT COUNT(*) FROM erabiltzailea"
    res = cur.execute(ag)
    emaitza = res.fetchone()
    print("ZERRENDA ZEMBAT")
    print(emaitza)
    con.commit()
    con.close()
    return emaitza
def erab_badago (erab):
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag = f"SELECT * FROM erabiltzailea WHERE izena='{erab}'"
    print(erab)
    res = cur.execute(ag)
    print(res)
    emaitza = res.fetchone() is not None
    print(emaitza)
    con.commit()
    con.close()
    return emaitza

def updatePasah(erab, pa):
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag = f" UPDATE erabiltzailea SET pasahitza='{pa}' WHERE izena='{erab}'"
    res = cur.execute(ag)
    con.commit()
    con.close()

def ezabatuErab(erab):
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag=f" DELETE FROM erabiltzailea WHERE izena='{erab}'"
    res=cur.execute(ag)
    con.commit()
    con.close()

def puntuazioaLortu (erab):
    print(erab)
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag = f"SELECT puntuazioa FROM erabiltzailea WHERE izena='{erab}'"
    res = cur.execute(ag)
    emaitza = res.fetchone()
    print(emaitza)
    con.commit()
    con.close()
    return emaitza

def administratzaileaDa (erab):
    print(erab)
    con = sqlite3.connect("taulak.db")
    # SQL kontsulten emaitzak egiteko behar den kurtsorea
    cur = con.cursor()
    ag = f"SELECT administratzailea FROM erabiltzailea WHERE izena='{erab}'"
    res = cur.execute(ag)
    emaitza = res.fetchone()
    print(emaitza)
    con.commit()
    con.close()
    return emaitza

if __name__=='__main__':
    #ezabatuTaula()
    createTable()
    erabGehitu("Miriam","1234", "Lucas", "12A")
    #erab_badago("Maria")
    #erab_badago("Miriamj")
#    ezabatuErab('')
   # ezabatuErab('Miri')
    #ezabatuErab('Miriam')
    #erab_pasahitza_lortu("Miriam")