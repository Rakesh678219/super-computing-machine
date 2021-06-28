
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input as mobilenet_v2_preprocess_input
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import streamlit as st
import streamlit.components.v1 as components
import time
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = "0"
from multiapp import MultiApp
from apps import home, test, foods, harmful_foods, project_credits

app = MultiApp()
app.add_app("Home", home.app)
app.add_app("Eye Checkup", test.app)
app.add_app("Healthy foods for eyes", foods.app)
app.add_app("Foods that are bad for eyes", harmful_foods.app)
app.add_app("Contact Page and Project Credits", project_credits.app)
app.run()

st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: #A9ADB0
        }
    </style>

    """,
    unsafe_allow_html=True,

)
st.write("#")
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)
