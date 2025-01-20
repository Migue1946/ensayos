
import streamlit as st
import pandas as pd
import plotly.express as px

import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import stats
#Cursera Colombia  Analisis de DataFrame"


df=pd.read_excel('C:/Users/Lenovo/Desktop/ENSAYOS/Ensayo.xlsx')
#print(df)
st.write(df)

mediat=df['tratado'].mean() #esta es la media. En describe figura como mean
mediac=df['control'].mean()

mediant=df['tratado'].median() # esta es la mediana. En describe en el valor que figura al 50%
medianc=df['control'].median()

df['tmedia']=mediat
df['cmedia']=mediac

ax=df.plot.line(x='sitio', y=['control','tratado','tmedia','cmedia'],linestyle='dashdot')
plt.plot(df['tratado'].mean(), color='blue',linestyle='dashdot',label='Mediana de Tratado')
#plt.show()
opciones = ['control','tratado','cmedia','tmedia',['control','tratado'],['cmedia','tmedia'] ]

with st.sidebar:
    parVariable=st.selectbox('Variable',options=opciones)

st.title('Datos del Ensayo')
fig= px.line(df,x='sitio',y= parVariable,title=f'{parVariable}')
st.plotly_chart(fig,use_container_width=True)