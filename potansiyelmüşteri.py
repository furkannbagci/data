import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\b_fur\OneDrive\Masaüstü\her şey\vs code\data miuu\denemeler\miuul_gezinomi.xlsx")
print(df[0:10])

uniqe_city = df["SaleCityName"].unique()
unique_concept = df["ConceptName"].unique()
concept_sale_count = df["ConceptName"].value_counts()
total_price_for_citys = df.groupby("SaleCityName")["Price"].sum()
total_price_for_concepts = df.groupby("ConceptName")["Price"].sum()
mean_price_for_citys = df.groupby("SaleCityName")["Price"].mean()
mean_price_for_concepts = df.groupby("ConceptName")["Price"].mean()
city_concept_kırılımı_price_mean = df.groupby(["SaleCityName","ConceptName"])["Price"].mean()

"""
#GÖREV 1 CIKTILARI 

print("\n unique şehirler: " , uniqe_city)
print("\n unique concepts: " , unique_concept)
print("\n concept satış sayıları: " , concept_sale_count)
print("\n şehirlere göre toplam satış: " , total_price_for_citys)
print("\n konseptlere göre toplam satış: " , total_price_for_concepts)
print("\n şehirlere göre ortalama satış: " , mean_price_for_citys)
print("\n konseptlere göre ortalama satış: " , mean_price_for_concepts)
print("şehir konseept kırılımına göre fiyat ortalaması: " ,city_concept_kırılımı_price_mean)
"""

#GÖREV 2 

def calc_EB_Score(col):
    if (col >= 0 and col < 7):
        return "LastMinuters"
    elif (col >=7 and col < 30):
        return "Potential_Planners"
    elif (col >= 30 and col < 90):
        return "Planners"
    elif (col >= 90):
        return "Early_Bookers"                     

df["EB_Score"] = df["SaleCheckInDayDiff"].apply(calc_EB_Score)       

print("\n",df[0:7],"\n")

#GÖREV 3 

mean_price_segmentation = df.groupby(["SaleCityName","ConceptName","EB_Score"]).agg({"Price":["mean","count"]}) 

#GÖREV 4

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price" : "mean"}).sort_values("Price", ascending=False)

#GÖREV 5

reset_indexl = mean_price_segmentation.reset_index(inplace=True ) 
print(reset_indexl)

#GÖREV 6

df["sales_level_based"] = df["SaleCityName"]+"_"+df["ConceptName"]+"_"+df["Seasons"]

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons","sales_level_based"]).agg({"Price" : "mean"}).reset_index().sort_values("Price",ascending=False)

#GÖREV 7

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], q=4 , labels=["D","C","B","A"]) 
agg_df.groupby("SEGMENT").agg({"Price":["mean","max","sum"]})


#GÖREV 8

new_antalya = "Antalya_Herşey Dahil_High"
new_girne_segment = "Girne_Yarım Pansiyon_Low"

a = df[df["sales_level_based"] == new_antalya]
print(f"\n ortalama antalya yüksek:  {a["Price"].mean()} ")


b = agg_df[agg_df["sales_level_based"] == new_girne_segment]
print(f"Girne_Yarım Pansiyon_Low yer alacağı segment:  {b["SEGMENT"].astype(str)}")
