student = ["s","b","c"]

for s in student:
    print(s.upper())


str = "hi my name is john and i am learning python"

#str metninin uzunluğunu len ile alıp range ile (0,43) formunda yazdırıyorum
print(range(len(str)))

#deneme fonksiyonu string değişkeninin uzunluğunu alıp her değer için sayı çift ise değere denk gelen indexi büyütür değilse küçültür
def deneme(string):
    text = ""
    for i in range(len(string)):
        if (i%2 == 0):
            text += string[i].upper()
        else:
            text += string[i].lower()
    print(text)        

deneme(str)
#üstteki örneğin enumarate ile yazılmış hali 
def enum(string):
    text =""
    for i,str in enumerate(string):
        if i%2 == 0:
            text += str.upper()
        else:
            text += str.lower()

    print(text) 
#enum("maraba efendim")                           
"""---------------------------------------------------------------------------------------------------------------------------------

#enumarate: otomatik counter/indexer ile for loop

students = ["ali","memed","ahmad"]

for index,studens in enumerate(students,1):#1 değeri indexin başlangıç deeğrini belirtir
    print(index,students)

---------------------------------------------------------------------------------------------------------------------------------"""
#ayrı ayrı listlelere kaydetme 
t=[]
c=[]
students = ["ali","memed","ahmad","furkan","john"]


def divide_students():
    for index,stud in enumerate(students):
        if index%2==0:
            t.append(stud)
            return t
        else:
            c.append(stud)  
            return c                        
divide_students()

#iki boyutlu listeye kaydetme
def divide(students):
    groups = [[],[]]
    for index,stud in enumerate(students):
        if index%2==0:
            groups[0].append(stud)
        else:
            groups[1].append(stud)
    print(groups)
    return groups           

divide(students)    

"""---------------------------------------------------------------------------------------------------------------------------------"""

#zip

isim = ["ali","memed","ahmad","furkan","john"]
soyisim = ["a","b","c","d","e"]
no = ["1","2","3","4","5"]
sss = list(zip(isim,soyisim,no))
print(sss)

"""---------------------------------------------------------------------------------------------------------------------------------"""

#LAMBDA , MAP , FİLTER,REDUCE
#lambda kullan at fonksiyon görevi görür
#map for döngüsü yerine kullanılabilir
#filter ile for içinde sorgulama yaparcasına döngüye alabiliyoruz

salaries = [1000,2000,3000]
def new_salary(x):
    return x*20

for salary in salaries:
    print(new_salary(salary))

#yukardaki ile aynı işlevi görecek fonksiyon:
a = list(map(new_salary,salaries))
print(a)

#ya da lambda ile new_salary fonksiyonun yerine fonk tanımlanabilir
a=list(map(lambda x:x*20,salaries))#fonksiyondaki gibi x değişkeni tanımlandı ve salaries listesine uygulandı
print(a)

b = list(filter(lambda x:x%3 == 0,salaries))#salaries listesinde 3 ile tam bölünebilenleri ayırır
print (b) 

from functools import reduce
c=reduce(lambda a,b: a+b,salaries)#salariesteki her elemana işlem uygular
print(c)