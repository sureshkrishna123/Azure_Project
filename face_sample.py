import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title("Face Recognition(Powered by Azure)")


st.header('Face Recognition:')

st.text("Using Azure I build to **_detect, identify and analyse_ faces** in images.")
st.text("Detect the objects in images")
uploaded_file = st.file_uploader("Choose a file")
image = Image.open(uploaded_file)

st.image(image, caption='Uploaded image')

select=st.selectbox("select what you want to find in the image" ,['Faces','Age & emotions ','objects'])

button_translate=st.button('Click me',help='To give the image')
