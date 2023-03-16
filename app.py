
import pickle
import streamlit as st
import numpy as np
import pyparsing
import pandas as pd
import matplotlib as plt
import seaborn as sns
from PIL import Image 
import tensorflow
from tensorflow.keras.models import load_model
import tensorflow as tf
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image 
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Lung Cancer Detection')




st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)

def loading_model():
    fp = "models/keras_model.h5"
    model_loader = load_model(fp)
    return model_loader

cnn = loading_model()
st.write("""
# Lung Cancer Detection using CNN and CT-Scan Images
""")



temp = st.file_uploader("Upload CT-Scan Image",type=['png','jpeg','jpg'])
if temp is not None:
    file_details = {"FileName":temp.name,"FileType":temp.type,"FileSize":temp.size}
    st.write(file_details)
    #temp = temp.decode()

buffer = temp
temp_file = NamedTemporaryFile(delete=False)
if buffer:
    temp_file.write(buffer.getvalue())
    st.write(image.load_img(temp_file.name))


if buffer is None:
    st.text("Oops! that doesn't look like an image. Try again.")

else:
    ved_img = image.load_img(temp_file.name, target_size=(224, 224))

    # Preprocessing the image
    pp_ved_img = image.img_to_array(ved_img)
    pp_ved_img = pp_ved_img/255
    pp_ved_img = np.expand_dims(pp_ved_img, axis=0)

    #predict
    hardik_preds= cnn.predict(pp_ved_img)
    print(hardik_preds[0])

    if hardik_preds[0][0]>= 0.5:
        out = ('I am {:.2%} percent confirmed that this is a Normal Case'.format(hardik_preds[0][0]))
        st.balloons()
        st.success(out)

    else: 
        out = ('I am {:.2%} percent confirmed that this is a Lung Cancer Case'.format(1-hardik_preds[0][0]))
        st.error(out)



    image = Image.open(temp)
    st.image(image,use_column_width=True)
  
              

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  

    
