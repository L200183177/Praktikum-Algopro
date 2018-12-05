##Activities 2, Alif Fauzia Rama Wahyu K
berkas = open("L200183177","w")
berkas.write("L200183177 \n")
berkas.write("27-05-2000 \n")
berkas.write("Alif Fauzia Rama Wahyu K \n")
berkas.write("Salatiga \n")
berkas.close()

import shelve
a = open("L200183177","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Alif")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

a = shelve.open("Alif")
 
print (a['b'][0])
print (a['b'][1])
print (a['b'][2])
print (a['b'][3])
