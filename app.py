import streamlit as st
import pickle
import numpy as np
from sklearn.metrics import r2_score
# Cargar el modelo y los objetos de preprocesamiento
with open('modelo/modelo_entrenado.pkl', 'rb') as f:
    model = pickle.load(f)

with open('modelo/scaler_km.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('modelo/le_model.pkl', 'rb') as f:
    le_model = pickle.load(f)

with open('modelo/le_color.pkl', 'rb') as f:
    le_color = pickle.load(f)

with open('modelo/le_country.pkl', 'rb') as f:
    le_country = pickle.load(f)

# Modelos y sus imágenes
models = {
    'Model S': 'https://i.blogs.es/efcca7/screenshot/1366_521.jpg',
    'Model 3': 'https://www.km77.com/images/medium/3/8/5/5/tesla-model-3-2021-gran-autonomia-frontal.353855.jpg',
    'Model X': 'https://hips.hearstapps.com/es.h-cdn.co/cades/contenidos/12966/sectionhero.jpg',
    'Model Y': 'https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2024/01/17/17055067065145.jpg'
}

# Estilo CSS
st.markdown("""
    <style>
        .img-container {
            text-align: center;
        }
        .img-container img {
            height: 150px; /* Fija la altura de las imágenes */
            width: auto;
            border-radius: 10px;
            object-fit: cover;
        }
        .selected {
            border: 3px solid #FF4B4B; /* Borde rojo para la selección */
            padding: 5px;
            border-radius: 10px;
        }
        .img-caption {
            margin-top: 5px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)


st.title("Predicción del Precio de TESLA")
st.image('https://mycaready.com/wp-content/uploads/2022/07/tesla-logo-rojo_BnFAmz92.jpg')
# Sección de inputs
st.header("Introduce las características del coche")

# Crear columnas para mostrar los modelos
col1, col2, col3, col4 = st.columns(4)

# Variable para guardar el modelo seleccionado
selected_model = st.session_state.get("selected_model", None)
# Mostrar imágenes con estilos dinámicos
with col1:
    st.markdown(f"""
        <div class="img-container">
            <img src="{models['Model S']}" alt="Model S">
            <div class="img-caption">Model S</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Seleccionar Model S"):
        st.session_state.selected_model = "Model S"

with col2:
    st.markdown(f"""
        <div class="img-container">
            <img src="{models['Model 3']}" alt="Model 3">
            <div class="img-caption">Model 3</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Seleccionar Model 3"):
        st.session_state.selected_model = "Model 3"

with col3:
    st.markdown(f"""
        <div class="img-container">
            <img src="{models['Model X']}" alt="Model X">
            <div class="img-caption">Model X</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Seleccionar Model X"):
        st.session_state.selected_model = "Model x"

with col4:
    st.markdown(f"""
        <div class="img-container">
            <img src="{models['Model Y']}" alt="Model Y">
            <div class="img-caption">Model Y</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Seleccionar Model Y"):
        st.session_state.selected_model = "Model Y"

# Inputs adicionales
year_input = st.number_input("Año del coche", min_value=2000, max_value=2025, step=1)
km_input = st.number_input("Kilometraje (km)", min_value=0, step=1000)
color_input = st.selectbox("Color del coche", le_color.classes_)
country_input = st.selectbox("País", le_country.classes_)

# Validar selección del modelo
if "selected_model" in st.session_state:
    model_encoded = le_model.transform([st.session_state.selected_model])[0]
    color_encoded = le_color.transform([color_input])[0]
    country_encoded = le_country.transform([country_input])[0]
    km_scaled = scaler.transform([[km_input]])[0][0]

    # Crear entrada para el modelo
    entrada_modelo = np.array([[model_encoded, year_input, km_scaled, color_encoded, country_encoded]])

    # Botón para predecir
    if st.button("Predecir Precio"):
        prediccion = model.predict(entrada_modelo)
        st.success(f"El precio estimado del coche es: {prediccion[0]:,.2f} €")

else:
    st.error("Por favor, selecciona un modelo antes de continuar.")
