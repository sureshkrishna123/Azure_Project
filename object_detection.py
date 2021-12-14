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

 


image_file =  st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
  img = Image.open(image_file)
  st.image(image_file,width=250,caption='Uploaded image')
  byte_io = BytesIO()
  img.save(byte_io, 'PNG')
  image = byte_io.getvalue()

select=st.selectbox("select what you want to find in the image" ,['Faces','Age & emotions ','objects'])

button_translate=st.button('Click me',help='To give the image')

if button_translate and image_file :
  def draw_face(img):



# Add your Computer Vision subscription key and endpoint to your environment variables.

        subscription_key = 'afac470736ce49ca8352ec7c83736fc7'
        endpoint = 'https://objectdetection21.cognitiveservices.azure.com/'

        analyze_url = endpoint + "vision/v3.1/analyze"  
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params = {'visualFeatures': 'Categories,Description,Color'}
        
        response = requests.post(analyze_url, headers=headers,params=params, data=image)
        response.raise_for_status()
        analysis = response.json()
        print(json.dumps(response.json()))
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
        response_image = requests.get(remote_image_url)
# Display the image and overlay it with the caption.
        aux_im = Image.open(BytesIO(response_image.content))
        plt.imshow(aux_im)
        plt.axis("off")
        _ = plt.title(image_caption, size="x-large", y=-0.1)
        plt.show()
   #image_data = open(image_file, "rb").read()

  image = draw_face(img)

  st.image(image, caption='Output image')
