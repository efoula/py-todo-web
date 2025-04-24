import streamlit as st
from PIL import Image

# with st.expander("Camera"):
#     camer_img = st.camera_input("Take a picture")

# if camer_img:
#     img = Image.open(camer_img)
#     gray_img = img.convert("L")
#     st.image(gray_img, caption="Gray Image", use_column_width=True)

uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert the image to grayscale
    gray_image = image.convert("L")
    st.image(gray_image, caption="Grayscale Image", use_container_width=True)