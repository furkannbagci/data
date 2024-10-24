import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#########################
#GENEL RESİM
#########################

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

def check_df(datafrmae,head=5):
    print("----shape-----")
    print(datafrmae.shape)
    print("----types-----")
    print(datafrmae.dtypes)
    print("----head-----")
    print(datafrmae.head(head))
    print("----tail------")
    print(datafrmae.tail(head))
    print("----na-------")
    print(datafrmae.isnull().sum())
    print("----quantiles-----")
    print(datafrmae.describe([0,0.05,0.50,0.95,0.99,1])) #0: Minimum değer (en düşük değer)0.05: %5'lik çeyrek (1. yüzdelik)0.50: Medyan (orta değer)0.95: %95'lik çeyrek (en yüksek değerlerden biri)0.99: %99'luk çeyrek (çok yüksek değerler)1: Maksimum değer (en yüksek değer)
check_df(df)    


#-------------------------------------------------------

#########################
#KATEGORİK DEĞİŞKEN ANALİZİ
#########################

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

catch_cols = [col for col in df.columns if str(df[col].dtype) in ["category","bool","object"]] #kategorik değişkenleri ve tipi kategorik olmayıp kategorik olanları (mesela bool) seçer 

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]] #değişken sayısı 10'dan küçük ve tipi float veya int olanları seçer

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]] #değ sayısı 20'den büyük tipi cat obj olanlar (category olmayanları elemek için)

catch_cols = catch_cols + num_but_cat #tüm kategorikleri topladık

#catch_cols = [col for col in catch_cols if col not in cat_but_car] #cat_but_car değişkenlerini elemek için for döngüsüne sokuyoruz (üsttekilerden sonra kullanılırsa üst. yoksayar)

#şimdi yapılanları fonk haline getirelim
print(catch_cols)
#ilgili değişkenin hangi değerleri old ve değerlerin yüzdeliğini veren fonk
def cat_summary (dataframe,col_name):


#değişken sayıları
    print(dataframe[col_name].value_counts())
    #yüzdelik dilim
    print(100 * dataframe[col_name].value_counts() /len(dataframe))
    
    #yukardakileri dataframe formunda yazdırmak için:
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "ratio(oran)":100*dataframe[col_name].value_counts()/len(dataframe)}))
    print("#############################")

    
for col in catch_cols:  #for döngüsü ile yakaladığımız kategorik değişkenlere fonksiyon uygulama
    cat_summary(df,col)


#yukardaki işlemi görsellleştiren fonksiyon:

def cat_summary_pct (dataframe,col_name,plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "ratio(oran)":100*dataframe[col_name].value_counts()/len(dataframe)}))
    print("#############################")

    if plot:
        sns.countplot(x=dataframe[col_name],data=dataframe) #kategorikleri sütun grafiğine dökme
        plt.show(block = True)

print(df.head())
#cat_summary_pct(df,"sex",plot=True)

for col in catch_cols:
    if df[col].dtypes == "bool": #eğer col bool türünde ise ekrana verme ve yazı yaz
        print("booooooooool")
        #ya da 
        df[col] = df[col].astype(int) #bool değeri int çevirip fonksiyonu kullanabilirim
        cat_summary_pct(df,col,plot=True) 
    else:
        cat_summary_pct(df,col,plot=True) 


#-----------------------------------------------

#######################
#SAYISAL DEĞİŞKEN ANALİZİ (ANALYSİS OF NUMERİCAL VARİABLES)
#######################

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df[["age","fare"]].describe().T  #istenilen sütunların özet bilgileri

catch_cols = [col for col in df.columns if str(df[col].dtype) in ["category","bool","object"]] #kategorik değişkenleri ve tipi kategorik olmayıp kategorik olanları (mesela bool) seçer 
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]] #değişken sayısı 10'dan küçük ve tipi float veya int olanları seçer
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]] #değ sayısı 20'den büyük tipi cat obj olanlar (category olmayanları elemek için)
catch_cols = catch_cols + num_but_cat #tüm kategorikleri topladık

num_cols = [col  for col in df.columns if df[col].dtypes in ["float64","int64"]] #sadece float ve int türünde olanları alır
num_cols = [col for col in num_cols if col not in catch_cols] #filtrelediğimiz sütunlar haricinde olan sayısal değişkenleri seçiyoruz

def num_summ(dataframe, numerical_cols, plot=False): #istenilen filtrelere göre fonksiyon
    quantiles = [0.10,0.30,0.50,0.70,0.90,1] #istenilen aralık
    print(dataframe[numerical_cols].describe(quantiles).T) #istenilen aralıkta özet gösterim 

    if plot: #veriyi tabloya dökme kısmı
        dataframe[numerical_cols].hist() #sütun gr şeklinde gösterme
        plt.xlabel(numerical_cols)
        plt.title(numerical_cols)
        plt.show(block=True)

for col in num_cols: #for ile istenilen veri türleri aarasında gezer
    num_summ(df,col,plot=True)
    print("##################################")    

#-----------------------------------------------

#####################################
#DEĞİŞKENLERİN YAKALANMASI VE İŞLEMLERİN GERÇEKLEŞTİRİLMESİ
#####################################

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

def grab_col_names(dataframe,cat_th = 10,car_th = 20):
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["object","category","bool"]]    
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes in ["int64","float"]]    
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ["object","category","bool"]]
    catch_cols = cat_cols + num_but_cat
    catch_cols = [col for col in  cat_cols if col not in cat_but_car]

    # numeric tespiti

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int64","float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]        

    print(f"Observation: {dataframe.shape[0]}") #hesaplanan değişkenleri yazdırdık
    print(f"veriables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(catch_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return catch_cols,num_cols,cat_but_car #hesapladığımız değerleri return ettik

help(grab_col_names) #fonksiyon içindeki yorum kısmını getirir (marabayın kısmı)

catch_cols,num_cols,cat_but_car = grab_col_names(df) #df adlı dataframe için değişken fonksiyon kullanarak atamaları yaptık 

#artık değişkenleri fonksiyon aracılığıyla atayabiliyor ve dışara fonksiyon çağırılarak atama işlemi yaılabiliyor


##########################
#HEDEF DEĞİŞKEN ANALİZİ(ANALYSİS OF TARGET VARİABLE)
##########################

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")


def grab_col_names(dataframe,cat_th = 10,car_th = 20):
    
    #kategorik tespiti
    
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["object","category","bool"]]    
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes in [int,float]]    
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ["object","category","bool"]]
    catch_cols = cat_cols + num_but_cat
    catch_cols = [col for col in  cat_cols if col not in cat_but_car]

    # numeric tespiti

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in [int,float]]
    num_cols = [col for col in num_cols if col not in catch_cols]

    return catch_cols,num_cols,cat_but_car #hesapladığımız değerleri return ettik

catch_cols,num_cols,cat_but_car = grab_col_names(df) #df adlı dataframe için değişken fonksiyon kullanarak atamaları yaptık 

for col in df.columns: #bool değişkenlerini int atadık
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

#HEDEF DEĞİŞKENİNİ KATEGORİK DEĞİŞKENLERİ İLE İNCELENMESİ

a=df.groupby("sex")["survived"].mean()
print(a)

#üstteki işlemi fonk aracılığı ile yapabiliriz

def target_summary_with_cat(dataframe,target,categorical_col):
    print(pd.DataFrame({"TARGET MEAN: ": dataframe.groupby(categorical_col)[target].mean()}).head(), end="\n\n")
target_summary_with_cat(df,"survived","sex")    
target_summary_with_cat(df,"survived","pclass")    

for col in num_cols:
    target_summary_with_cat(df,"survived",col)

#-------------------------------------------------------

#HEDEF DEĞİŞKENİNİ SAYISAK DEĞİŞKENLERİ İLE İNCELENMESİ

print("#############################################")
print(df.groupby("survived").agg({"age":"mean"}))

def target_summary_with_num(dataframe,target,numerical_col):
    print(pd.DataFrame(dataframe.groupby(target).agg({numerical_col:"mean"})).head(), end="\n\n")

for col in num_cols:
    target_summary_with_num(df,"survived",col)      


#-------------------------------------------------------
################################
#KORELASYON ANALİZİ (ANALYSİS OF CORRELATİON)
################################

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = pd.read_csv(r"C:\Users\b_fur\OneDrive\Masaüstü\her şey\vs code\data miuu\data.csv")

#df.columns = [col[:10] for col in df.columns]  # Sütun isimlerini kısalt
df = df.iloc[:,1:-1]

num_cols = [col for col in df.columns if df[col].dtypes in [int,float]]

#korelasyon ile birbiri arasındaki ilişkileri görüyoruz (+1'e yaklaştıkça ilişki pozitif yönde kuvvetli artarsa artar gibi -1'e yaklaştıkça ise ters orantı vardır)

corr = df[num_cols].corr() #korelasyon hesabı
print(df.head().transpose()) #transpose (tersini) alarak yazdırdık düzgün görünmesi için
print("###########################")
print(corr.head().transpose())

sns.set_theme(rc={"figure.figsize":(12,12)})
sns.heatmap(corr,cmap = "RdBu")
plt.show()

#--------------------------------------------------------------

#YÜKSEK KORELASYONLU (BENZER) DEĞİŞKENLERİN SİLİNMESİ

# kolerasyon değerlerinin mmutlağını alıyorum (işlem kolaylığu için)
cor_matrix = df[num_cols].corr().abs()

#satır ve sütunlarda aynı değerler olduğundan aynı sonucu 2 kere görmemek için eleme yapmalıyız
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool_))
print(df.shape)
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90)] #korelasyon oranı 0.90'dan büyük olanlar
print(drop_list)
df.drop(drop_list,axis=1,inplace=True) #korelasyon oranı yüksek olan sütunları kaldırıyoruz
print(df.shape)

#fonksiyon haline getirmek için:

# yüksek korelasyonlu değerleri silmek
def high_correlated_cols(dataframe,corr_th=0.90):
    num_cols = [col for col in df.columns if df[col].dtypes in [int,float]]
    corr = dataframe[num_cols].corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>corr_th)]
    dataframe.drop(drop_list,axis=1,inplace=True)
    return drop_list,dataframe

# yapılan işlemler sonrası heat_map gösterme fonksiyonu
def heat_map_show(dataframe,plot=True):
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in [int,float]]
    cor = dataframe[num_cols].corr()
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set_theme(rc={"figure.figsize":(15,15)})
        sns.heatmap(cor,cmap="RdBu")
        plt.show()
print(df.describe())
print("#####################")
heat_map_show(df)
high_correlated_cols(df)
heat_map_show(df)
