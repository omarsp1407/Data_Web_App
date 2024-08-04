import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

car_data = pd.read_csv('C:/Users/osp14/Documents/PythonProjects/Data_Web_App/Data_Web_App/dataset/vehicles_us.csv') # leer los datos

# Crear un encabezado
st.header('Generador de Histogramas con Plotly Express')

# Función para crear el histograma
def crear_histograma():
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    return fig

# Función para crear el gráfico de dispersión
def crear_grafico_dispersion():
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión    
    return fig

# Crear un botón que al hacer clic construye el histograma
if st.button('Generar Histograma'):
    histograma = crear_histograma()
    st.plotly_chart(histograma)

# Crear un botón que al hacer clic construye el diagraa de dispersion
if st.button('Generar Diagrama de dispersion'):
    dispersion = crear_grafico_dispersion()
    st.plotly_chart(dispersion)