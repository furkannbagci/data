#tek boyutlu ve index bilgilerini içerir
import pandas as pd

s = pd.Series([10,23,34,23])
print(s)

s.index #index bilgisi
s.dtype #verinin tip bilgisini verir
s.size #eleman sayısı
s.ndim #boyut bilgisi
s.values #değerlere erişim
s.head(3) #ilk 3 veriyi alır
s.tail(3) #sondan 3 veriyi alır
s.shape #satır sütun bilgisini verir

#------------------------------------------------------------------------

#READİNG DATA

dt = pd.read_csv("Kitap1.csv")
print(dt.head(3))
#pandas cheatsheet (pandas fonksiyonlar için dökümantasyon )

#------------------------------------------------------------------------

import seaborn as sns

df = sns.load_dataset("titanic")#seaborn kütüphanesinde bulunan hazır veri setlerine erişim

df.info()#veriler hakkında bilgileri verir satır, sütun ,dolu ,tür
df.columns#değişkenlerin isimleri
df.describe().T #özet bilgi (t ile transpozunu alıyoruz daha okunabilir yapmak için max mean gibi) 
print(df.describe().T )

df.isnull().values.any()#values değerlerinde eksik var mı sorgusu için kullanılır
df.isnull().sum()#herbir değişkende kaç adet eksik olduğunu hesaplar
df["sex"].value_counts()#sex sütununun kaç türe ayrıldığını ve her türden kaç adet olduğunu gözlemlemek

#------------------------------------------------------------------------
#selection in pandas (pandasta seçim işlemleri)

import seaborn as sns
df = sns.load_dataset("titanic")
df[0:13] #indexi 0 dan 13 e kadar olan verileri gösterir

df.drop([0,2,4],axis=0).head() #0,2 ve 4.indexleri siler ve en baştan birkaç veri gösterir
#axis = 0 için satırları = 1 için sütunları seçer
 
delete_index = [0,2,4] #silinecek indexleri değişkene atayabiliriz
df.drop(delete_index,axis=0,inplace=True) #inplace=true ifadesi ile yaptığımız değişiklikleri kaydedebiliriz

#değişkeni indexe çevirmek:

# age sütununa erişmek için:
df["age"]
df.age.head()

df.index = df.age #index yerine age ataması
df.drop("age", axis=1,inplace=True)##age sütununu kalıcı silme işlemi

#indexi değişkene çevirme:

df["age"]=df.index #eğer age değişkeni yoksa oluşturur ve değer olarak index değerlerini atar
print(df.head())

#ikinci yol ise:
df = df.reset_index()#index değerini eski haline getirir ve age değişkenini sütuna ekler
print(df.head())

#------------------------------------------------------------------------

#değişkenler üzerinde işlemler

import seaborn as sns
df = sns.load_dataset("titanic")

df["age"] #pandas serisini ifade eder tek boyutlu
df[["age"]] #dataframe değerlerine erişir 2 boyutlu
df["age2"] = df["age"]*2

df.loc[:,df.columns.str.contains("age")]#loc ile seçme işlemi yapıyoruz : ile tüm satırları, df.--.contains("age") ile de içinde age değişkenini barındıran sütunları alır

print( df.loc[:,~df.columns.str.contains("age")].head()) # " ~ " işareti ile seçilen öğeler dışındaki verileri alırız 

#------------------------------------------------------------------------

# iloc ve loc 

import seaborn as sns

df = sns.load_dataset("titanic")

#iloc : integer based selection
df.iloc[0:3] #indexlerde 0 dan 3 e kadar olan indexleri alır
df.iloc[0:3,0:3] #str değer girersek hata alırız

#loc : label based selection
df.loc[0:3] #indexlerde 0 dan 3 e kadar 3 de dahil olmak üzere seçim yapar
df.loc[0:3,"age"] #loc ile str seçimi yapılabilir 
col_names = ["age","sex"]
df.loc[0:3,col_names] #col_names listesinden seçim yapılabilir

#------------------------------------------------------------------------

#koşullu seçimler (conditional selection)

import seaborn as sns

df = sns.load_dataset("titanic")
df["embark_town"].value_counts() #embark_town sütununda kaç adet value değeri olduğunu sayar


df[df["age"] > 50]["age"].count() #yaşı 50'den büyük olanları count ile sayıyoruz 

#loc ile
df.loc[df["age"] > 50,["age","class"]] #yaşı 50'den büyük olanların yaşlarını ve sınıflarını alıyoruz

df_new = df.loc[(df["age"] > 50) & 
       (df["sex"] == "male") &  #yaşı 50'den büyük, erkek, ve Southampton Cherbourg yerlerinden gelenleri seçiyoruz ve onları yaş sınıf ve embark_town sütunlarını yazdırıyoruz 
       ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),["age","class","embark_town"]]#koşul belirtirken () içinde belirtmemiz gerekir 
print(df_new)

#------------------------------------------------------------------------

#TOPLULAŞTIRMA ve GRUPLAMA (AGGREGATİON ve GROUPİNG)

import seaborn as sns
df= sns.load_dataset("titanic")

df["age"].mean() #yaşların ortalamması

df.groupby("sex")["age"].mean() #cinsiyete göre sınıflandırıp yaşların ortalamasını alor
df.groupby("sex").agg({"age":["mean","max"]}) #agg ile yaşın ortalaması ve maks değerlerini alır

a=df.groupby(["sex","class","embark_town"]).agg({"age":["mean"],  #cinsiyet sınıf ve town'a göre yaşın ve ölüm durumunun ortalamasını alır
                                               "survived":["mean"],
                                               "sex":"count"})#cinsiyet sayıları
print(a)

#------------------------------------------------------------------------

#PİVOT TABLE

import seaborn as sns

df = sns.load_dataset("titanic")

df.pivot_table("survived","sex","embarked") #value değeri olarak survive satırda sex sütunda ise embarked değerlerini gösterir
                                            #ve kesişimlerinde survived değerlerinin ortalamasını alır

df.pivot_table("survived","sex","embarked" , aggfunc="std") #survive değerlerine standart sapma hesabı yaptırır
df.pivot_table("survived","sex",["embarked","class"]) #embarked ile classı tek bölg alır

df["new_age"] = pd.cut(df["age"],[0,10,18,25,40,100]) #new_age sütununa yaşın verilen değerlere bölünmüş halini atar
df.pivot_table("survived","sex",["new_age","class"]) #verilen yaş aralıklarına göre ortalama yaşama iht hesaplanır

pd.set_option("display.width",500) #çıktı genişliğini 500px olarak ayarlar

#------------------------------------------------------------------------

#APPLY & LAMBDA 

import seaborn as sns

pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df["age2"]=df["age"]*2
df["age3"]=df["age"]*5

#içinde age barındıran değişkinlerin tümüne işlem uygulamak için:

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10 #age bulunduran sütunlardaki değerleri 10 a böler

#aynı işlemi apply ve lambda ile yapalum:
df[["age","age2","age3"]].apply(lambda x:x/10) #verilen listedekilere lambda ile tek seferlik işlem uygula
#veya
df.loc[:,df.columns.str.contains("age")].apply(lambda x:x/10) #içinde age bulunduran sütunlara işlem uygula

#dışardan tanımlanan fonksiyonu apply içine yazabiliriz
def stndrt_sclr(col_name):
    return (col_name - col_name.mean())/col_name.std()
df.loc[:,df.columns.str.contains("age")].apply(stndrt_sclr) #içinde age bulunduran sütunlara stndrt_sclr fonksiyonunu uygula

#yapılanları kaydetmek için:
df.loc[:,df.columns.str.contains("age")] = df.loc[:,df.columns.str.contains("age")].apply(stndrt_sclr)

print(df.head())

#------------------------------------------------------------------------

#BİRLEŞTİRME (JOİN) İŞLEMLERİ

import seaborn as sns
import numpy as np

df = sns.load_dataset("titanic")
pd.set_option("display.width",500)

m = np.random.randint(1,30,size=(5,3)) #1 ile 30 arasında random seçilen sayılarla 5'e 3'lük matris oluşturur

df1 = pd.DataFrame(m,columns=["var1","var2","var3"])
df2 = df1 + 99

pd.concat([df1,df2], ignore_index=True)#df1 dataframe ile df2 yi birleştirir indexleri önemsemez 0 dan başlatmak yerine olduğu gibi devam eder

#MERGE İLE BİRLEŞTİRME:

df11 = pd.DataFrame({"employees":["john","dennis","mark","maria"],
                     "group":["accounting","engineering","engineering","hr"]})

df12 = pd.DataFrame({"employees":["john","dennis","mark","maria"],
                     "start_date":[2010,2009,2014,2019]})

pd.merge(df11,df12) #iki listeyi de birleştirir
pd.merge(df11,df12,on="employees") #employees'e göre birleştirir
df13=pd.merge(df11,df12)

df14 = pd.DataFrame({"group":["accounting","engineering","hr"],
                     "manager":["caner","mustafa","berkcan"]})

#müdür bilgilerini de eklemek için df13 ile df14'ü merge ile bilrleştiririz merge ortak değişkenler üzerinden birleştirmme yapar
df15=pd.merge(df13,df14)
df15.index = df15.index + 1
print(df15) 


