import numpy as np


a = [1,2,3,4]
b = [2,3,4,5]

ab=[a[i]*b[i] for i in range(len(a))]
print(ab)

#yukardaki işlemi numpy ile yapalım
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

print(a*b)

#----------------------------------------------------------------------------------
#numpy array oluşturma

np.array([1,2,3,4])
np.zeros(10,dtype=int)
a = np.random.randint(0,10,size=10)#0 ile 10 arasında 10 tane random sayı üretir
print(a)
b = np.random.normal(10,4,(1,5))#ortalaması 10 standart sapması 4 olan 1 satır 3 sütun için random sayı üretir
print(b)


#----------------------------------------------------------------------------------

#ndim : boyut sayısı
#shape : boyut bilgisi
#size : toplam eleman bilgisi
#d.type : array veri tipi

#----------------------------------------------------------------------------------

#reshape :  eleman sayısı yeterli ise matrisi yeniden boyutlandırma

#----------------------------------------------------------------------------------

#İNDEX SEÇİMİ (İNDEX SELECTİON)
a = np.array([[1,2,3],
             [1,2,3],
             [1,2,3]])
print(a[:,0] )#bütün satırların 0. sütununu verir
print(a[0:2 , 0:1])#satırlarda 0 dan 2 ye kadar git sütunlarda ise 0 dan 1 e kadar git (2 ve 1 hariç)


#----------------------------------------------------------------------------------

#FANCY İNDEX

v = np.arange(0,30,3)#0 dan 30 a kadr 30 hariç olmak üzere 3 er arttırarak array ekle
catch = [1,2,3]
v[catch]#catch içinde belirtilen indexleri alır
print(v)
print(v[catch])

#----------------------------------------------------------------------------------

#KOŞULLU İŞLEMLER

v = np.array([1,2,3,4,5,6])

#3'ten küçük elemanları almak için:
[v<3]#true false olarak döndürür
print(v[v<3])

#----------------------------------------------------------------------------------

#MATEMATİKSEL İŞLEMLER

v = np.array([1,2,3,4,5])
v = v*2 + 4 #işlemi tüm elemanlara uygular

np.subtract(v,1)#her değerden 1 çıkarma işlemi
np.add(v,1)#her değerle 1 toplama işlemi
np.mean(v)#ortalama alma işlemi
np.sum(v)#değerlerin toplamı
np.min(v)#min değer
np.max(v)#maks değer
np.var(v)#varyans alma işlemleri

#----------------------------------------------------------------------------------

#denklem çözme 

#  5*x0 + x1 = 12
#  x0 + 3*x1 = 10

#yukardaki denklemin çözümü:

a = np.array([[5,1],[1,3]])#5 ve 1 x0'in katsayıları 1 ve 3 ise x1'in katsayılarıdır
b = np.array([12,10])#denklemlerin eşitlik kısmı

sonuc = np.linalg.solve(a,b)
print(sonuc)