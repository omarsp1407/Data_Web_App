import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

car_data = pd.read_csv('C:/Users/osp14/Documents/PythonProjects/Data_Web_App/Data_Web_App/dataset/vehicles_us.csv') # leer los datos

# Crear un encabezado
st.header('Generador de Histogramas con Plotly Express')

# Función para crear el histograma
def crear_histograma():
    datos = np.random.randn(1000)  
    df = pd.DataFrame({'Valores': datos})
    fig = px.histogram(df, x='Valores', nbins=30, title='Histograma de Valores Aleatorios')
    
    return fig

# Crear un botón que al hacer clic construye el histograma
if st.button('Generar Histograma'):
    histograma = crear_histograma()
    st.plotly_chart(histograma)