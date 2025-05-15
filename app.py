# app.py
import streamlit as st
from prediction import predict_water_safety
from analyse import run_analysis_app

st.set_page_config(page_title="Analyse et Prédiction Qualité de l'eau", layout="wide")

st.title(" Analyse et Prédiction de la Qualité de l'eau")

# إعداد الحالة (state)
if "show_analysis" not in st.session_state:
    st.session_state.show_analysis = False

# زر لإظهار التحليلات
if st.button("Afficher les analyses"):
    st.session_state.show_analysis = True

# عرض التحليلات إذا الحالة مفعلة
if st.session_state.show_analysis:
    run_analysis_app()

# Sidebar ديال التنبؤ
st.sidebar.header("Entrer les valeurs pour prédiction")

features = [
    "aluminium", "ammonia", "arsenic", "barium", "cadmium", "chloramine", "chromium",
    "copper", "flouride", "bacteria", "viruses", "lead", "nitrates", "nitrites",
    "mercury", "perchlorate", "radium", "selenium", "silver", "uranium"
]

input_data = {}
for feature in features:
    input_data[feature] = st.sidebar.number_input(f"{feature.capitalize()}", min_value=0.0, format="%.5f")

if st.sidebar.button("Prédire la qualité de l'eau"):
    result = predict_water_safety(input_data)
    if result == 1:
        st.success(" L'eau est sûre à consommer.")
    else:
        st.error(" L'eau n'est pas sûre à consommer.")
