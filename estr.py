
import streamlit as st
import pandas as pd
import plotly.express as px

import numpy as np
from matplotlib import pyplot as plt


#Cursera Colombia  Analisis de DataFrame"


df=pd.read_excel('C:/Users/Lenovo/Desktop/ENSAYOS/Ensayo.xlsx')

opciones = ['control','tratado']

with st.sidebar:
    parVariable=st.selectbox('Variable',options=opciones)

st.title('Datos del Ensayo')
#st.write(df)
'''

fig= px.bar(df,x='sitio',y= parVariable,title=f'{parVariable}')
st.plotly_chart(fig, use_container_width=True)

'''
fig, ax=plt.subplots(1,1)
ax.scatter(x=df['sitio'],y = df[parVariable])
ax.set_xlabel('sitio')
ax.set_ylabel('opciones')
ax.set_title('Sitios vs Opciones')

st.pyplot(fig)
