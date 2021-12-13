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

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title('Test the API powered by azure')
st.sidebar.subheader('select API want to test')
app_mode = st.sidebar.selectbox('Choose the App mode',
['Face Recognization','Translator']
)


if app_mode=='Face Recognization':
  st.image(os.path.join('./images','facial-recognition-software-image.jpg'),use_column_width=True )
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

        subscription_key = 'ea8c44f876804e43ab35a26a09d59da5'  
        BASE_URL = "https://recognition-ai.cognitiveservices.azure.com/" + '/face/v1.0/detect'  
        headers = {
        # Request headers
        'Content-Type': 'application/octet-stream', 
        'recognitionModel': 'recognition_01' ,
        'Ocp-Apim-Subscription-Key': subscription_key,
        'detectionModel': 'detection_01',
        }
        response = requests.post(BASE_URL, headers=headers, data=image)
        faces = response.json()
        print(faces)
        def getRectangle(faceDictionary):
            rect = faceDictionary['faceRectangle']
            left = rect['left']
            top = rect['top']
            bottom = left + rect['height']
            right = top + rect['width']
            return ((left, top), (bottom, right))


        output_image = Image.open(BytesIO(image))
    #   For each face returned use the face rectangle and draw a red box.
        draw = ImageDraw.Draw(output_image)
        for face in faces:
            draw.rectangle(getRectangle(face), outline='red')
        return output_image
   #image_data = open(image_file, "rb").read()

    image = draw_face(img)

    st.image(image, caption='Output image')

if app_mode =='Translator':
   
    st.image(os.path.join('./images','unnamed.png'),use_column_width=True )
    st.markdown("<h1 style='text-align: center; color: skyblue; '>Welcome to our page Translate a language now just in no time: </h1>", unsafe_allow_html=True)

    st.markdown("Translator is a cloud-based machine translation service you can use to translate text in with a simple REST API call. The service uses modern neural machine translation technology and offers statistical machine translation technology. Custom Translator is an extension of Translator, which allows you to build neural translation systems. The customized translation system can be used to translate text with Translator or Microsoft Speech Services")
    
    st.markdown("For more documentation on language support in Azure:[click here](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support)")
    st.markdown('---')

    detect=st.text_input('Enter the text to detect (No language Restriction):')

    detect_select=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=1)

    if detect_select == 'arabic':
        detect_lang= 'ar'
    elif detect_select == 'bangla':
        detect_lang= 'bn'
    elif detect_select == 'chinese':
        detect_lang= 'lzh'
    elif detect_select == 'dutch':
        detect_lang= 'nl'
    elif detect_select == 'english':
        detect_lang= 'en'
    elif detect_select == 'french':
        detect_lang= 'fr'
    elif detect_select == 'german':
        detect_lang= 'de'
    elif detect_select == 'greek':
        detect_lang= 'el'
    elif detect_select == 'hindi':
        detect_lang= 'hi'
    elif detect_select == 'hungarian':
        detect_lang= 'hu'
    elif detect_select == 'indonesian':
        detect_lang= 'id'
    elif detect_select == 'irish':
        detect_lang= 'ga'
    elif detect_select == 'italian':
        detect_lang= 'it'
    elif detect_select == 'japanese':
        detect_lang= 'ja'
    elif detect_select == 'kannada':
        detect_lang= 'kn'
    elif detect_select == 'korean':
        detect_lang= 'ko'
    elif detect_select == 'malayalam':
        detect_lang= 'ml'
    elif detect_select == 'nepali':
        detect_lang= 'ne'
    elif detect_select == 'portuguesei':
        detect_lang= 'pt'
    elif detect_select == 'punjabi':
        detect_lang= 'pa'
    elif detect_select == 'russian':
        detect_lang= 'ru'
    elif detect_select == 'spanish':
        detect_lang= 'es'
    elif detect_select == 'tamil':
        detect_lang= 'ta'
    elif detect_select == 'telugu':
        detect_lang= 'te'  
    elif detect_select == 'turkish':
        detect_lang= 'tr'
    elif detect_select == 'urdu':
        detect_lang= 'ur'          


    button_detect=st.button('Click me',help='To detect language')

    if button_detect and detect:
        import requests, uuid, json

        # Add your subscription key and endpoint
        subscription_key ="6f7488eb5fe442a8adc4cdcd4cd50474"
        endpoint = "https://api.cognitive.microsofttranslator.com/"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "eastus"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'to': [detect_lang]
        }
        constructed_url = endpoint + path

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': detect
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response123 = request.json()


        st.success(json.dumps(response123, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    elif button_detect:
        st.error("!! Please enter input in any language")

    st.markdown('---')
    
