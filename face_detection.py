#Code in Google Colab
#used by importing azure modules

pip install --upgrade azure-cognitiveservices-vision-face

import cgitb 
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
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
import numpy as np
import matplotlib.pyplot as plt



# This key will serve all examples in this document.
KEY = "ea8c44f876804e43ab35a26a09d59da5"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://recognition-ai.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
image_url = 'https://lh3.googleusercontent.com/pw/AM-JKLWihuQfkjmAu7AG5xRaoCnB9PI5VI6dZGcXhqVtIMk6L9swLa0M8WziWt0uVOTjTEY03WKKzAppzFt62mbpYT9C5x5n-gI0S8TmfOzUOg2X6CceLspAVqWSKyXN96r7C6YNHSGXUw7xm1wK2utNAAjNXg=w2249-h1686-no?authuser=0'
image_name = os.path.basename(image_url)

response_detected_faces = face_client.face.detect_with_url(
    image_url,
    detection_model='detection_01',
    recognition_model='recognition_04',
    return_face_attributes=['age', 'emotion'],

)
print(response_detected_faces)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(respone_image.content))
draw = ImageDraw.Draw(img)




for face in response_detected_faces:
    age = face.face_attributes.age
    emotion = face.face_attributes.emotion
    neutral = '{0:.0f}%'.format(emotion.neutral * 100)
    happiness = '{0:.0f}%'.format(emotion.happiness * 100)
    anger = '{0:.0f}%'.format(emotion.anger * 100)
    sandness = '{0:.0f}%'.format(emotion.sadness * 100)

    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

    draw.text((right + 4, top), 'Age: ' + str(int(age)), fill=(255, 255, 255))
    draw.text((right + 4, top+35), 'Neutral: ' + neutral, fill=(255, 255, 255))
    draw.text((right + 4, top+70), 'Happy: ' + happiness, fill=(255, 255, 255))
    draw.text((right + 4, top+105), 'Sad: ' + sandness, fill=(255, 255, 255))
    draw.text((right + 4, top+140), 'Angry: ' + anger, fill=(255, 255, 255))
    

    
plt.imshow(img)

