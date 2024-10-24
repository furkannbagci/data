import pandas as pd
import seaborn as sns
import numpy as np


#1.SORU

df = sns.load_dataset("car_crashes")
print(df.head())

num_columns = [col.upper() for col in df.columns if df[col].dtype != "O"]

print(num_columns)

#--------------------------------------------------------------------------

#2.SORU

df = sns.load_dataset("car_crashes")

flag_columns = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
print(flag_columns)

#--------------------------------------------------------------------------
#3.SORU

df = sns.load_dataset("car_crashes")
og_list = ["abbrev","no_previous"]

new_col = [col for col in df.columns if col not in og_list]
new_df =  df[new_col] 
print(new_df)

#--------------------------------------------------------------------------
#4.SORU

df = sns.load_dataset("titanic")

sex_count = df["sex"].value_counts() #cinsiyet sayıları

df.nunique() #unique değerlerin sayısı
df["pclass"].nunique() #pclassın uniq değ sayısı
df[["pclass","parch"]].nunique() #pclassın ve parchın uniq değılım sayısı

df["embarked"].dtype #embarked değişkeninin tipini öğrenme
df["embarked"] = df["embarked"].astype("category") #embarked değişkeninin tipini category olarak değiştirme
embarked_c = df.loc[(df["embarked"]=="C")] #embarked değeri C olanların bilgileri  veya : ( df[df["embarked"]=="C"] )
embarked_not_s = df.loc[(df["embarked"] != "S")] #embarked değeri S olmayanların bilgileri

female_30 = df.loc[(df["age"] < 30 ) & (df["sex"] == "female")] #yaşı 30dan küçük kadınlar ya da (df[(df["age"] <30]) & (df["sex"] == "female"))
fare500_age70 = df.loc[(df["age"] > 70) | (df["fare"] > 500)] #yaşı 70'ten büyük veya fare değeri 500'den büyükler

nullvalues = df.isnull().sum() #her sütun için boş değerlerin sayısı

df.drop("who",axis=1,inplace=True) #2ho sütununu kalıcı olarak silme

type(df["deck"].mode())
df["deck"].isnull() #deck sütununun boş değerleri
df["deck"] = df["deck"].fillna(df["deck"].mode()[0]) #deck sütununundaki boş değerlerin yerine deck sütununun ortalamasını koy
#deck tipi seri olduğundan index belirtmek gerekiyor
df["age"]=df["age"].fillna(df["age"].median())
işlemler = ["sum","count","mean"]
surv_group = df.groupby(["pclass","sex"]).agg({"survived": ["mean","count","sum"]}) #survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerleri

#soru 16
def soru_16(age):
    if age <30:
        return 1 
    else: 
        return 0       
df["new_flag"] = df["age"].apply(lambda x : soru_16(x))
df["new_flag"] = df["age"].apply(lambda x : 1 if x < 30 else 0)
#---

df2 = sns.load_dataset("tips")

time_cal = df2.groupby(["time"]).agg({"total_bill": ["min","max","sum","mean"]}) #time değerlerine göre total_bill e işlem uygulama
time_day_cal = df2.groupby(["time","day"]).agg({"total_bill": ["min","max","mean"]}) #time ve day değerlerine göre total_bill e işlem uygulama

filt = df2[(df2['sex'] == "Female") & (df2['time'] == "Lunch")]
#obsorved ile varsayılan değişkenin değişmeyeceğini belirtiyoruz
female_lunch = filt.groupby(["day"],observed=False).agg({"total_bill": ["min","max","mean"], #koşul için df2[()] parantez içine if olmadan belirtilir 
    "tip":["min","max","mean"]}) #filt ile belirtilen koşul üzerinde işlem yapılır

filt_bill_mean = df2.loc[(df2["size"]<3) & (df2["total_bill"]>10),"total_bill"].mean() #filtrelemeye göre total_bill değerlerinin ortalaması

df2["total_bill_tip_sum"]=df2["total_bill"]+df2["tip"] #tip ile total_bill in toplamını veren sütun oluşturma
anotherdf=df2.sort_values(["total_bill_tip_sum"]).head(30) #total_bill_tip_sum değerlerini sort_values ile küçükten büyüğe sıralar ve head(10) ile ilk 10 değeri gösterir
#head(30) yerien [:30] kullanılabilir
df3 = pd.DataFrame(anotherdf) #yeni bir dataframe oluşturup onun içine anotherdf verilerini ataması
df3.shape #df3'ün satır ve sütun sayılarını gösterir
