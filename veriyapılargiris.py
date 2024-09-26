long_str = """amdasşldmasşdmasdlasmdşalmdşaslmdşaslmdaldmalsşd"""
strr = "maraba"

#slice
strr[0:2]#sıfırdan 2 ye kadar olan dizi değerlerini alır

#karakter sorgulama
strr = "maraba"
"ma" in strr

#metodları görmek için
dir(int) #int için kullanılabilen metodlar

#LİSTELER
nam = [1,2,3,"a","b",True,[1,3,4]]
nam[6][2] #4 sayısına erişir 
#append sona ekler
#pop indeks değerine göre siler

#SÖZLÜK DİCTİONARY

#key-value
dictionary = {"REG":"regression",
              "LOG":"logistic regression"}
dictionary["REG"] #REG keyinde denk gelen regression value sini alır

dic2 = {"reg":["regress",32],
        "log": 132}

#update ile güncelleme key değeri yoksa ekleme işlemi yapılır
dic2.update({"rell":["aaa",121]})
print(dic2)
#DEMET TUPLE (değiştirilemez)
t = ("ahmad",1,23)

#SETLER
set1 = set(["aa","bb",3])
set2 = set(["aa","bb",2])

#difference
print(set1.difference(set2))