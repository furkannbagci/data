#VERİ GÖRSELLEŞTİRME : MATPLOTLİB & SEABORN

#MATPLOTLİB

#Kategorik değişkenler için : sütun grafiği => countplot , bar (seaborn , matplotlib)
#Sayısal değişkenler için : hist , boxplot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.max_columns",None) 
pd.set_option("display.width",500)


#KATEGORİK DEĞİŞKEN GÖRSELLEŞTİRME

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None) #null değerleri göstermez
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df["sex"].value_counts() #sex sütunundaki value değerlerini ve her değerden kaç tane old verir
df["sex"].value_counts().plot(kind="bar") #plot ile grafik yapıyor ve kind ile grafiğin türünü belirliyoruz
plt.show()


#-----------------------------------------------------------------------------

#SAYISAL DEĞİŞKEN GÖRSELLEŞTİRME

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None) 
pd.set_option("display.width",500)

df = sns.load_dataset("titanic")

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"]) 
plt.show()

#-----------------------------------------------------------------------------

#MATPLOTLİB ÖZELLİKLERİ

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.max_columns",None) 
pd.set_option("display.width",500)

#plot:

x = np.array([1,8])
y = np.array([0,150])

plt.plot(x,y) #x ile y arasına çizgi çeken grafik

plt.plot(x,y, "o") #x ile y koordinatlarına denk gelen yerlere nokta koymak

a = np.array([1,5,7,12])
b = np.array([1,2,3,4])

plt.plot(a,b)
plt.show()


#-----------------------------------------------------------------------------

#marker:

y = np.array([1,2,3,4,5]) 

plt.plot(y , marker = "*") #her index için verilen değeri grafiğe döker

#-----------------------------------------------------------------------------


#line:

y = np.array([1,2,3,4,5]) 
plt.plot(y , linestyle="dotted") #linestyle ile çizginin biçimini değiştirebiliyoruz

#-----------------------------------------------------------------------------

#multiple lines: 

x = np.array([2,23,32,42,51]) 
y = np.array([1,3,4,5]) 

plt.plot(x)
plt.plot(y,linestyle="dotted")

plt.title("ana başlık isimlendirmesi")
plt.xlabel("x ekseni isimlendirme")
plt.ylabel("y ekseni isimlendirme")
plt.grid() #arka plana ızgara yerleştirme

#-----------------------------------------------------------------------------


#subplots: çoklu grafik gösterimi

x = ([33,44,55,66,33,22,66])
y = ([22,45,34,23,67,78,90])

plt.subplot(1,3,1) #1 satır 3 sütunlu tablonun ilki 
plt.title("1")
plt.plot(x,y)

x = ([3,43,5,62]) #ikincisi
y = ([42,45,34,23])

plt.subplot(1,3,2)
plt.title("2")
plt.plot(x,y)

x = ([33,44,55,66]) # üçüncü
y = ([33,33,22,66])


plt.subplot(1,3,3)
plt.title("3")
plt.plot(x,y)


#-----------------------------------------------------------------------------

#SEABORN 

#kategorik değişkenler:

from matplotlib import pyplot as plt
df = sns.load_dataset("tips")

df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df) #gösterilecek değeri x ile veri alınacak dataframei de data ile gösterilir

plt.show()

#---------------------------------------------------
#sayısal değişkenler:


from matplotlib import pyplot as plt
df = sns.load_dataset("tips")

sns.boxplot(x=df["total_bill"])

df["total_bill"].hist()
plt.show()

