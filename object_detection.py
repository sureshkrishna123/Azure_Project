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
import json



st.title("Face Recognition(Powered by Azure)")


st.header('Face Recognition:')

st.text("Using Azure I build to **_detect, identify and analyse_ faces** in images.")
st.text("Detect the objects in images")

 


url_file =  title = st.text_input('Paste image URL')


select=st.selectbox("select what you want to find in the image" ,['Faces','Age & emotions ','objects'])

button_translate=st.button('Click me',help='To give the image')

if button_translate and url_file :
   def draw_face():


        subscription_key = 'afac470736ce49ca8352ec7c83736fc7'
        endpoint = 'https://objectdetection21.cognitiveservices.azure.com/'
# Add your Computer Vision subscription key and endpoint to your environment variables.

        analyze_url = endpoint + "vision/v3.1/analyze"
# Set image_url to the URL of an image that you want to analyze.

        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params = {'visualFeatures': 'Categories,Description,Color'}
        data = {'url': url_file}
        response = requests.post(analyze_url, headers=headers,params=params, json=data)
        response.raise_for_status()

         # The 'analysis' object contains various fields that describe the image. The most
         # relevant caption for the image is obtained from the 'description' property.
        analysis = response.json()
        print(json.dumps(response.json()))
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
        response_image = requests.get(url_file)
        # Display the image and overlay it with the caption.

        aux_im = Image.open(BytesIO(response_image.content))
        
        #plt.imshow(aux_im)
        #plt.axis("off")
        #_ = plt.title(image_caption, size="x-large", y=-0.1)
        #plt.show()

   draw_face()
   st.image(aux_im, caption=image_caption)
