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

'''
# Anuncios de ventas de coches
### Selecciona gráfico:
'''

table_checkbox = st.checkbox('Visualizar Datos')  # crea botón para la tabla
# crear un botón para histograma
hist_checkbox = st.checkbox('Construir histograma')
# crear una casilla de verificación para grafico de dispersión
disp_checkbox = st.checkbox('Construir un gráfico de dispersión')

if table_checkbox:
    st.write('## Visualización de datos')

    # Filtro por condición
    condition_filter = st.multiselect(
        'Seleccione condición de coche', options=car_data['condition'].unique())

    # Filtro por precio
    price_filter = st.slider('Rango de precio', int(car_data['price'].min()), int(
        car_data['price'].max()), (int(car_data['price'].min()), int(car_data['price'].max())))

    # Filtro por año del modelo
    year_filter = st.slider('Rango de año del modelo', int(car_data['model_year'].min()), int(
        car_data['model_year'].max()), (int(car_data['model_year'].min()), int(car_data['model_year'].max())))

    # Aplicar los filtros
    filtered_data = car_data[
        (car_data['price'] >= price_filter[0]) & (car_data['price'] <= price_filter[1]) &
        (car_data['model_year'] >= year_filter[0]) & (
            car_data['model_year'] <= year_filter[1])
    ]

    if condition_filter:
        filtered_data = filtered_data[filtered_data['condition'].isin(
            condition_filter)]

    # Mostrar la tabla filtrada
    st.write(filtered_data)

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
