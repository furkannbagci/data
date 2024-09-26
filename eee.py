import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

a=df.iloc[0:3,0:3]
print(a)