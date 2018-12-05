##Activities 3, Alif Fauzia Rama Wahyu K
import shelve

data = open("L200183177", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Alif")
data["newdata"] = [NIM, TL, Nama, Kota]
data.close()
