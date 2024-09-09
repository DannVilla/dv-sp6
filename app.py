import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

### Limpieza de data ###
# Convierte a datetime
car_data['date_posted'] = pd.to_datetime(
    car_data['date_posted'], format='%Y-%m-%d')

# Eliminar valores NaN
car_data = car_data.dropna(subset=['model_year'])

# Convertir a int
car_data['model_year'] = car_data['model_year'].astype(int)
###

table_checkbox = st.checkbox('Visualizar Datos')  # crea botón para la tabla
# crear un botón para histograma
hist_checkbox = st.checkbox('Construir histograma')
# crear una casilla de verificación para grafico de dispersión
disp_checkbox = st.checkbox('Construir un gráfico de dispersión')

if table_checkbox:  # si la casilla de verificación está seleccionada
    st.write(
        '## Visualización de datos')  # mensaje al abrir botón

    st.write(pd.DataFrame(car_data))  # Tabla de Datos

if hist_checkbox:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write(
        '## Histograma de anuncios de venta de coches por Kilometraje')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# streamlit run app.py

if disp_checkbox:  # si la casilla de verificación está seleccionada
    st.write('## Dispersión Precio vs Kilometraje')

    # Crear gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price',
                     color='model_year')

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
