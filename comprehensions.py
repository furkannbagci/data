#LİST COMPREHENSİON


salaryies = [100,200,600,800]
liste=[]
for salary in salaryies:
    if salary<300:
        liste.append(salary*2)
    else:
        liste.append(salary)    
print(liste)        

#yukardaki işlemi tek satırda yapmak için:
liste = [(salary*2) if salary < 300 else salary for salary in salaryies] #aynı işlex = [(salary*2) for salary in salaryies if salary < 300](sadece if varsa)
print(liste)

#----------------------------------------------------------------------------------------------------

#dlictionary comp

dictionary = {"a":1,
              "b":2,
              "c":3}

dictionary.keys()#keylere erişim
dictionary.values()#valuelere erişim
dictionary.items()#keylere ve valuelere erişim

#işlem yapmak için:

liste = {k:v*2 for (k,v) in dictionary.items()}#value değerlerini 2 ile çarp

liste2 = {k.upper() :v for (k,v) in dictionary.items()}#key değerlerini büyütür 

print(liste)
print(liste2)

#----------------------------------------------------------------------------------------------------

#çift sayıların karesi alınacak keyler orj değerleri valueler ise karesi alınmış değerler olarak sözlüğe eklenecek

numbers = range(0,10)
new_dict = {}

for n in numbers:
    if (n%2 == 0):
        new_dict[n]=n**2
print(new_dict)

#aynı şeyi comp ile yapalım
new_dict2 = {n:n**2 for n in numbers if(n%2 == 0)}
print(new_dict2)

#----------------------------------------------------------------------------------------------------

#veri setindeki değişkenlerin isimlerini değiştirmek

#seaborn kütüp import edip sns adıyla kullanıyoruz 
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns#df deki başlıkları alır
print(df)

#herbir başlığı büyütüp a listesine ekliyor ve yazdırıyoruz
a=[]
for col in df.columns:
    a.append(col.upper())
print(a)    

#comp ile yapımı:
df.columns = [col.upper() for col in df.columns]
print(df.columns)

#----------------------------------------------------------------------------------------------------

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = ["flag_" + col if "ins" in col else "no_flag_"+col for col in df.columns ]
print(df.columns)

#----------------------------------------------------------------------------------------------------
#nümaratik olan başlıkların valuelerinde değer atamak

import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df)

num_columns = [col for col in df.columns if df[col].dtype != "O"]#sadece obj olmayanları yani sadece sayısal değişkenlerin başlıklarını listeye atıyoruz (abbrev sütunu alınmadı)
soz ={} #dict tanımlama
agg_list = ["mean","min","max","sum"]#fonksiyon isimlerini listeye atama

for col in num_columns:
    soz[col] = agg_list#soz dictine key olarak col girip value değerlerine agg_list değerlerini girmek
print(soz)

#aynı şeyi comp ile yapalum

soz = {col : agg_list for col in num_columns}#col ile key değerlerini atıyor ve agglisti de val olarak ekliyor 

print(df[num_columns].head())#data frame içinden num_columns(sayısal değişkenler) olanları seçer ve head fonk ile sadece başını yazdırır

fonkdeneme = df[num_columns].agg(soz)#soz deki değişkenler eğer num_columns da varsa onlara soz içindeki fonksiyonları (agg_list) uygular (mean = ortlama alma gibi)
print(fonkdeneme)
