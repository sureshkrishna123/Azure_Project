import streamlit as st
import pandas as pd
import numpy as np
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

if button_translate and uploaded_file:
    
    KEY = "ea8c44f876804e43ab35a26a09d59da5"

    # This endpoint will be used in all examples in this quickstart.
    ENDPOINT = "https://recognition-ai.cognitiveservices.azure.com/"

    
    constructed_url = ENDPOINT + KEY
    

    

    response_detected_faces = face_client.face.detect_with_stream(
        image=image,
        detection_model='detection_03',
        recognition_model='recognition_04',
        return_face_landmarks=True
    )

    if not response_detected_faces:
        raise Exception('No face detected')

    print('Number of people detected: {0}'.format(len(response_detected_faces)))

    print(vars(response_detected_faces[0]))
    print(vars(response_detected_faces[0].face_landmarks).keys())
    print(response_detected_faces[0].face_landmarks.mouth_left)

    img =Image.open(image)
    draw = ImageDraw.Draw(img)

    for face in response_detected_faces:
        rect = face.face_rectangle
        left = rect.left
        top = rect.top
        right = rect.width + left
        bottom = rect.height + top
        draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

        # mark the noise tip
        x = face.face_landmarks.nose_tip.x
        y = face.face_landmarks.nose_tip.y
        draw.rectangle(((x, y), (x, y)), outline='white', width=7)

        # draw the bounding box around the mouth
        mouth_left = face.face_landmarks.mouth_left.x, face.face_landmarks.mouth_left.y
        mouth_right = face.face_landmarks.mouth_right.x, face.face_landmarks.mouth_right.y
        lip_bottom = face.face_landmarks.under_lip_bottom.x, face.face_landmarks.under_lip_bottom.y
        draw.rectangle((mouth_left, (mouth_right[0], lip_bottom[1])), outline='yellow', width=2)

    st.image(img, caption='Output image')
