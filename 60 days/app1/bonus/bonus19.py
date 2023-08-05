import streamlit as st
import PIL.Image

st.subheader("Color to gray")


with st.expander("Start the camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")
    #print(camera_image)

with st.expander("Upload an image"):
    # Upload an image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    #print(uploaded_file)
    if uploaded_file:
        gray_img = PIL.Image.open(uploaded_file).convert('LA')
        st.image(gray_img)

if camera_image:
    img = PIL.Image.open(camera_image)
    gray_img = img.convert('LA')
    st.image(gray_img)