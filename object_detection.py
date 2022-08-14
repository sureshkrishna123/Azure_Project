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

st.set_page_config(layout="wide")
st.sidebar.image('images/Azure_Image.png', width=300)
st.sidebar.header('A website using Azure Api')
st.sidebar.markdown('Face Api,Translator Api')


app_mode = st.sidebar.radio(
    "",
    ("About Me","Object Detection"),
)


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('N.V.Suresh Krishna | sureshkrishnanv24@gmail.com https://github.com/sureshkrishna123')

if app_mode =='About Me':
    st.image('images/wp4498220.jpg', use_column_width=True)
    st.markdown('''
              # About Me \n 
                Hey this is ** N.V.Suresh Krishna **. \n
                
                
                Also check me out on Social Media
                - [git-Hub](https://github.com/sureshkrishna123)
                - [LinkedIn](https://www.linkedin.com/in/suresh-krishna-nv/)
                - [Instagram](https://www.instagram.com/worldofsuresh._/)
                - [Portfolio](https://sureshkrishna123.github.io/sureshportfolio/)
                - [Blog](https://ingenious-point.blogspot.com/)\n
                If you are interested in building more about Microsoft Azure then   [click here](https://azure.microsoft.com/en-in/)\n
                ''')
    if app_mode =='Object Detection':
    
    st.image(os.path.join('./images','object.jpg'),use_column_width=True )
    st.markdown("<h1 style='text-align: center; color: skyblue; '> Object Recognition </h1>", unsafe_allow_html=True)

    st.title("Object Recognition(Powered by Azure)")

    st.markdown("Using Azure I build to **_Object_ detection** , it identify and analyse the image.")
    st.text("Detect the objects in images")

    url_file =  title = st.text_input('Paste image address URL')
    st.text("Example :- https://www.intelligentliving.co/wp-content/uploads/2019/12/sculptures-reclaimed-materials-brianmock8_201911323127.jpg")
    button_translate=st.button('Click me',help='To give the image')

    if button_translate and url_file :
   
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
        captio=st.subheader(image_caption)
        st.image(aux_im, caption=image_caption)
