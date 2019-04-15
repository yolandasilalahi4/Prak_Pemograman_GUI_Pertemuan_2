Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Windows\SysWOW64>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD6
4)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> pins = {"Yolanda": 1234, "Febri": 3333, "Silalahi": 9999}
>>> pins["Yolanda"]
1234
>>> type(pins["Yolanda"])
<class 'int'>
>>> pins.keys()
dict_keys(['Yolanda', 'Febri', 'Silalahi'])
>>> pins.values()
dict_values([1234, 3333, 9999])
>>> pins["Morlee"] = 7777
>>> pins
{'Yolanda': 1234, 'Febri': 3333, 'Silalahi': 9999, 'Morlee': 7777}
>>> pins.pop("Morlee")
7777
>>> pins
{'Yolanda': 1234, 'Febri': 3333, 'Silalahi': 9999}
>>> pins["Elok"] = AB123
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'AB123' is not defined
>>> pins["Elok"] = 'AB123'
>>> PINS
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'PINS' is not defined
>>> pins["Elok"] = 'AB123'
>>> pins
{'Yolanda': 1234, 'Febri': 3333, 'Silalahi': 9999, 'Elok': 'AB123'}
>>> masukan =input("Masukan Nama Anda :")
Masukan Nama Anda :Yolanda
>>> bilangan = input("Masukan angka :")
Masukan angka :100
>>> print(masukan)
Yolanda
>>> type(masukan)
<class 'str'>
>>> bilangan = int(input("masukan angka :"))
masukan angka :99
>>> type(bilangan)
<class 'int'>
>>> print(bilangan**2)
9801
>>> bilangan= float(input("masukan angka :"))
masukan angka :10
>>> print(bilangan/2)
5.0
>>> bilangan = float(input("masukan angka :"))
masukan angka :9.5
>>> type(bilangan)
<class 'float'>
>>> print(bilangan/2)
4.75
>>> pins
{'Yolanda': 1234, 'Febri': 3333, 'Silalahi': 9999, 'Elok': 'AB123'}
>>> pins.value()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'value'
>>> pins.values()
dict_values([1234, 3333, 9999, 'AB123'])
>>> kode = 9999
>>> kode in pins.values()
True
>>> kode = 1111
>>> kode in pins.values()
False
>>> if 1<5:
...  print("Yes")
... else:
...  print("No")
...
Yes
>>>
>>> if 1==5:
...  print("Benar")
... else:
...  print("Salah")
...
Salah
>>> user_input = float(input("Masukan angka :"))
Masukan angka :77
>>> if user_input >100:
...  print("Greater")
... else:
...  print("Smaller")
...
Smaller
>>> if user_input >100:
...  print("Lebih Besar")
... else user_input == 100:
  File "<stdin>", line 3
    else user_input == 100:
                  ^
SyntaxError: invalid syntax
>>> if user_input >100:
...  print("Lebih Besar")
... elif user_input == 100:
...  print("Sama Dengan")
... else:
...  print("Lebih Kecil")
...
Lebih Kecil
>>> user_input = float(input("Masukan aAngka :"))
Masukan aAngka :100
>>> if user_input >100:
...  print("Lebih Besar")
... elif user_input == 100:
...  print("Sama Dengan")
... else:
...  print("Lebih Kecil")
...
Sama Dengan
>>> def printing():
...  print("Hello")
...  print("Dunia")
...
>>> printing()
Hello
Dunia
>>> def luas_persegi(sisi):
...   luas = sisi * sisi
...   return luas
...
>>> luas_persegi(9)
81
>>> def luas_segitiga(alas,tinggi):
...   luas = (alas*tinggi)/2
...   print("Luas Segitiga : %d" %luas)
...
>>> luas_segitiga(100,50)
Luas Segitiga : 2500
>>> def hitung_umur(tahun):
...   umur = 2019-tahun
...   print("Umur Saya : %d" %umur)
...
>>> hitung_umur(1999)
Umur Saya : 20
>>>
>>>