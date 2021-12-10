import streamlit as st
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from io import BytesIO
from PIL import Image
from PIL import ImageDraw




st.title("Face Recognition(Powered by Azure)")


st.header('Face Recognition:')

st.text("Using Azure I build to **_detect, identify and analyse_ faces** in images.")
st.text("Detect the objects in images")

 
image_url=st.text_input('Movie title', 'Life of Brian')

image_file =  st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
  img = Image.open(image_file)

  st.image(image_file,width=250,caption='Uploaded image')


select=st.selectbox("select what you want to find in the image" ,['Faces','Age & emotions ','objects'])

button_translate=st.button('Click me',help='To give the image')

if button_translate and image_file :

   def draw_face(img):

        subscription_key = 'ea8c44f876804e43ab35a26a09d59da5'  
        BASE_URL = "https://recognition-ai.cognitiveservices.azure.com/" + '/face/v1.0/detect'  
        headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',  
        'Ocp-Apim-Subscription-Key': subscription_key,
        }
        response = requests.post(BASE_URL,  headers=headers, data=img)
        faces = response.json()
        print(faces)
        def getRectangle(faceDictionary):
            rect = faceDictionary['faceRectangle']
            left = rect['left']
            top = rect['top']
            bottom = left + rect['height']
            right = top + rect['width']
            return ((left, top), (bottom, right))

        output_image = Image.open(BytesIO(img))
    #   For each face returned use the face rectangle and draw a red box.
        draw = ImageDraw.Draw(output_image)
        for face in faces:
            draw.rectangle(getRectangle(face), outline='red')
        return output_image
   #image_data = open(image_file, "rb").read()

   image = draw_face(img)

   st.image(image, caption='Output image')
