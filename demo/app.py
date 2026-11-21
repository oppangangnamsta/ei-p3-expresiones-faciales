"""Prototipo del espejo inteligente (Streamlit + webcam).

Todo se procesa en local y no se guarda ninguna imagen.
Ejecutar desde la raíz del repo: streamlit run demo/app.py
"""
import streamlit as st

st.set_page_config(page_title="Espejo inteligente", layout="centered")
st.title("Espejo inteligente")

st.sidebar.header("Privacidad y control")
enabled = st.sidebar.toggle("Activar adaptación por expresión facial", value=False)
show_debug = st.sidebar.checkbox("Mostrar probabilidades (modo demo)")
st.sidebar.caption(
    "El sistema reconoce expresiones observables, no emociones. "
    "Las imágenes se procesan en este dispositivo y no se guardan."
)

# TODO:
# 1. Capturar frames de la webcam (cv2.VideoCapture o streamlit-webrtc)
# 2. preprocess.detect_and_align -> modelo -> calibrate.apply_temperature
# 3. AdaptationPolicy.update(probs) y mostrar la sugerencia (si la hay) con botones
#    "Sí" / "No, gracias" / "No volver a sugerir"
# 4. Si show_debug, mostrar las probabilidades por clase y la confianza
st.info("Prototipo en construcción.")
