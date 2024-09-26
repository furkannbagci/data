print("sad","bad",sep="  _ayırma_  ")


#fonksiyon yazıp değerleri fonk dışında atayıp ,return sayesinde, kullanabilme
def calculate(a, b,c):
    a =a*2
    b = a*4
    c = 122
    output = (a+b)/c
    print(output)
    return a,b,c,output
    

a1,b1,c1,o1 = calculate(2,3,4)
print(a1)


def cal2(d,e):
    return d*e*e

#fonksiyon içinde fonk kullanma
def tsubasa(a,b,c,d,e):
    x = calculate(a,b,c)
    y = cal2(d,e)
    print(x)

tsubasa(1,1,1,1,1)

#hatalı
def deneme(a,b):
    deneme(a/b)

deneme(10,2)    