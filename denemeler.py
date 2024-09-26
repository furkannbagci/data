#2.SORU
text = "The goal is to turn data into information, and information into insight."
liste = []
for i in range(len(text)):
    text = text.upper()
    text=text.replace(".","")
    text=text.replace(",","")
    liste.append(text)        

liste = text.split(" ")
print(liste)
print(text) 
#-------------------------------------------------------------------------------------------------

#3.SORU
list = ["D","A","T","A","S","C","İ","E","N","C","E"]
eleman_sayısı=0
data_listesi = []
for index,eleman in enumerate(list):
    eleman_sayısı+=1
    if(index==0):
        print("0.eleeman: ",index,eleman)
    if(index == 10):
        print("10.eleman: ",index,eleman)
    if(index<4):
        data_listesi.append(eleman) 
    if(index == 8):
        list.pop(index)
        list.append("NN")
        list.insert(8,"N")
        print(list)    

print("eleman sayısı : ",eleman_sayısı)
print(data_listesi)

#-------------------------------------------------------------------------------------------------

#4.SORU

dict ={"christian": ["america",18],
       "daisy":["england",12],
       "antonio":["spain",22],
       "dante":["italy",25]}

dict.keys()#keylere erişim
dict.values()#val erişim       
for i in dict:
    a=dict[i]
    print(i)#key
    print(a)#value

print(dict)#eski
dict["daisy"]=["england",13]#güncelleme
dict["ahmet"]=["turkey",24]#ekleme
dict.pop("antonio")#silme
print(dict)#yeni

#-------------------------------------------------------------------------------------------------

#SORU 5

l = [2,13,18,93,22]
cift = []
tek = []
def ayrım():
    for i in l:
        if( i%2==0):
            cift.append(i)
        else:
            tek.append(i)    
    return cift,tek
    print("ciftler: ",cift)
    print("tekler: ",tek)

ayrım()    
#-------------------------------------------------------------------------------------------------

#SORU 6

students = ["ali","vali","bali","cali","dali","sali"]
müh=[]
tıp=[]
for index,ogr in enumerate(students):
    if(index<3):
        müh.append(ogr)
        print("müh fak.",index+1,".öğrenci: ",müh[index])
    else:
        tıp.append(ogr)  
        print("tıp fak.",(-1)*(3-(index+1)),".öğrenci: ",tıp[index-3])

#-------------------------------------------------------------------------------------------------

#SORU 7

derskodu = ["aaaaaaa","bbbbbb","ccccccccc","dddddd"]
kredi =[3,4,6,7]
kontejan = [30,75,23,12]

cümle = list(zip(derskodu,kredi,kontejan))

for derskodu,kontejan,kredi in cümle:
    print(f"kredisi ",kredi, " olan ",derskodu," kodlu dersin kontejanı ", kontejan)
    

#-------------------------------------------------------------------------------------------------
#SORU 8

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

kaps = kume1.issuperset(kume2)
dif = kume2.difference(kume1)
same = kume1.intersection(kume2)

#kapsıyorsa ortak;kapsammıyorsa farklılıkları yazdırma
if(kaps):
    print(same)
else:
    print(dif)    

print("küme 1: ", kume1)
print("küme 2: ",kume2 ,"\n")

print("farklar: ",dif)
print("aynılar: ",same,"\n")

print("kapsama :" , kaps)

