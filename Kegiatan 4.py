Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Alif Fauzia Rama Wahyu K"
>>> NIM = 177
>>> Tinggi = 1.77
>>> Berat = 68
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Because the "Aku" data is written in parentheses
>>> Aku[0]
2000
>>> # Because the first object in "Aku" data is "TahunLahir", The value of "TahunLahir" is 2000
>>> a = NIM % 4; Aku[a]
68
>>> # Because the remaining result of 177 divided by 4 is 0, so the result of Aku[a] is 68
>>> type(Aku[a])
<class 'int'>
>>> # Because the value of "TahunLahir" is 0, 0 is an integer data type
>>> Aku[a:4]
(68, 1.77, 177)
>>> # Because the 3 object in "Aku" data is "Berat", "Tinggi", and "NIM"
>>> type(Aku[4])
<class 'str'>
>>> # Because the fifth object in the "Aku" data is "Nama", The value of "Nama" is "Alif Fauzia Rama Wahyu K" that it is a string data type
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Because tuple element is cannot be changed
>>> type(Data)
<class 'list'>
>>> # Because the "Data" data is written in square brackets
>>> type(Data[4])
<class 'str'>
>>> # Because the fifth object in the "Data" data is "Nama", the value of "Nama" is "Alif Fauzia Rama Wahyu K" that it is a string data type
>>> Data[4][5]
'F'
>>> # Because there is no object in sixth object
>>> Data[4][a:6]
'lif F'
>>> # Because there is only "Nama" object
>>> Data[0] = 'ok'; Data
['ok', 68, 1.77, 177, 'Alif Fauzia Rama Wahyu K']
>>> # Because the first object already changed with "ok"
>>> Data[-a]
'Alif Fauzia Rama Wahyu K'
>>> # Because the first object in the "Data" is "Nama", the value of "Nama" is "Alif Fauzia Rama Wahyu K"
>>> range(a)
range(0, 1)
>>> # Because in the "a" data there is only 1 object
