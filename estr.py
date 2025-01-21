
import streamlit as st
import pandas as pd
import plotly.express as pxx

import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import stats
#Cursera Colombia  Analisis de DataFrame"


df=pd.read_excel('C:/Users/Lenovo/Desktop/ENSAYOS/Ensayo.xlsx')

opciones = ['control','tratado']

with st.sidebar:
    parVariable=st.selectbox('Variable',options=opciones)

st.title('Datos del Ensayo')
st.write(df)


fig= pxx.line(df,x='sitio',y= parVariable,title=f'{parVariable}')
st.plotly_chart(fig, use_container_width=True)


