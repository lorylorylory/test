import pandas as pd
import numpy as np
import re
df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\清洗\\水星记2.csv', encoding='utf-8-sig')
df['comment'] = df['comment'].str.strip('[]').astype(str)
df['comment'].replace('', np.nan, inplace=True)
df.dropna(subset=['comment'], inplace=True)
df.to_csv("C:\\Users\\lory\\\Desktop\\pythonProject1\\分词\\水星记3.csv", index=False)