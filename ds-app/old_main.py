import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
sns.set(font_scale=2)

# dfの表示
'''
## 10日間の気温の推移（表）

* day : 日
* temperature : 気温
* temperature_change : 前日の気温からの変化

'''
day_array = np.array([1,2,3,4,5,6,7,8,9,10])
temperature_array = np.array([10,9,10,12,14,15,13,13,16,18])
temperature_change_array = np.diff(temperature_array, prepend=10)

df = pd.DataFrame({
    'day': day_array,
    'temperature': temperature_array,
    'temperature_change' : temperature_change_array
})

df

# グラフの表示
'''
## 10日間の気温の推移（グラフ）
'''
df.set_index('day', inplace=True)
st.line_chart(df)


# fig = plt.figure(figsize=(8,8))
# ax = plt.axis
# plt.plot(day_array, temperature_array, color='red')
# plt.plot(day_array, temperature_change_array, color='green')
# plt.title('temperatures of last 10 days')
# plt.xlabel('day')
# plt.ylabel('temperature')
# st.pyplot(fig)