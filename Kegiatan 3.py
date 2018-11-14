Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Alif Fauzia Rama Wahyu K"
>>> NIM = "L200183177"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Because the "X" data had changed to integer data type
>>> type(b)
<class 'int'>
>>> # Because the "Nama" data has a "len" instruction
>>> a / b
49.041666666666664
>>> # Because the result of 1177 divided by 24 is 49.041666666666664
>>> a // b
49
>>> # because the meaning of "//" is division with rounding down
>>> 10 * (a - 999)
1780
>>> # Because the meaning of "a" minus 999 is 178, after that it will multiplied by 10 and the result is 1780
>>> b ** 2
576
>>> # Because the meaning of "**" is square
>>> a % b
1
>>> # Because the meaning of "%" is remaining of the result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Because "12.5" is a decimal number
>>> a / c
94.16
>>> # Because the result of 1177 divided by 12.5 is 94.16
>>> a // c
94.0
>>> # Because the meaning of "//" is division with rounding down and the operand type is writed in decimal number
>>> a % c
2.0
>>> # Because the meaning of "%" is remaining of the result
>>> c > b
False
>>> # Because the "b" data has a bigger value than the "c" data
>>> type(c > b)
<class 'bool'>
>>> # Because "True" or "False is a boolean data type
>>> a > b and b > c
True
>>> # Because in "and" operator symbol, if "True" meet with "True", the result is "True"
>>> a > 1000 or b < 10
True
>>> # Because in "or" operator symbol, if "False" meet with "False", the result is "False"
