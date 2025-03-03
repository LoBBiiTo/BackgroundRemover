import streamlit as st
from PIL import Image
from rembg import remove
import io
import onnxruntime as ort

# Funciones

def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    processed_image = remove_background(image)
    return processed_image

def remove_background(image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)
    processed_image_bytes = remove(image_bytes.read())
    return Image.open(io.BytesIO(processed_image_bytes))

# Front

st.markdown("<h1 style='text-align: center; font-family: sans-serif; font-size: 50px;'>BACKGROUND REMOVER</h1>", unsafe_allow_html=True)
st.header(body="",divider="rainbow")
st.header(body="")
st.image("icon/logo.png", use_container_width=True, clamp=True)
st.subheader(body="",divider="rainbow")
st.subheader("Carga una imagen", help="El fondo será removido automáticamente")
uploaded_image = st.file_uploader("Elegi una imagen...", type=["jpg","jpeg","png"], accept_multiple_files=False)

if  uploaded_image is not None:

    st.image(uploaded_image, caption="Imagen cargada", use_container_width=True, clamp=True)
    
    remove_button = st.button("Remover fondo")
    
    if remove_button:
        
        processed_image = process_image(uploaded_image)
        st.image(processed_image, caption="Imagen sin fondo", use_container_width=True, clamp=True)
        processed_image.save("imagen_sin_fondo.png")
        
        with open("imagen_sin_fondo.png", "rb") as file:
            image_data = file.read()
        st.download_button("Descargar imagen sin fondo", data=image_data, file_name="imagen_sin_fondo.png")


