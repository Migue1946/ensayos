import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import stats
#Cursera Colombia  Analisis de DataFrame"


df=pd.read_excel('Ensayo.xlsx')

df_melt=pd.melt(df,id_vars='sitio', value_vars=['tratado','control'])


plt.figure(figsize=(10,6))
plt.boxplot(df_melt.loc[df_melt['variable']=='tratado','value'], label=['Tratado'])

plt.title('Ensayos de Fertilización')
plt.xlabel('Tratamientos')
plt.ylabel('Rendimientos')
plt.show()

# queria hacer 2 cajas pero no pude...