import requests
import io
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import scipy.stats
sns.set(font_scale=2)
sns.set_style("whitegrid")

'''
## 新型コロナウイルス感染症の札幌市内発生状況
### 日毎の陽性患者数（表）

'''

url = 'https://ckan.pf-sapporo.jp/dataset/c89f65e7-45a8-4ab2-b94d-494ae192c70f/resource/b83606f6-3aa2-4e0c-8a1a-509dd36be2ae/download/patientssummary.csv'

res = requests.get(url).content
df = pd.read_csv(io.StringIO(res.decode('utf-8')))

df['日付'] = pd.to_datetime(df['日付'].str[:10])
df['小計'] = df['小計'].astype(int)
df

'''
### 日毎の陽性患者数（グラフ）

'''
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)
plt.xlabel('day')
plt.ylabel('numbers of patients')
ax.plot(df['日付'], df['小計'], color='red')

ax.xaxis.set_major_locator(ticker.MultipleLocator(60))
plt.setp(ax.get_xticklabels(), rotation=0)

plt.tight_layout()
st.write(fig)
