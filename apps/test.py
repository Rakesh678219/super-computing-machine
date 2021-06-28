import json
import cv2
import numpy as np
from numpy.core.fromnumeric import resize
import streamlit as st
from keras.models import model_from_json


def app():
    st.title("Eye Disease Classification With ML")
    st.header("Test Your Eyes Today !! ")

    def draw_all(
        key,
        plot=False,
    ):
        col1, col2, col3 = st.beta_columns([1, 4.5, 1])

        with col1:
            st.write("")

        with col2:
            st.image('rvce.png')

        with col3:
            st.write("")

        st.write(
            """
            # Minor Project On ML
            
            """
        )
        st.write("#")
        st.header("Contributed by")
        st.write(
            """
            **Pavankalyan D S  - 1RV18EC108**\n
            **Rakesh Reddy P -  1RV18EC109**\n
            **Prajwal  B  Raj -  1RV18EC111** \n
            **Pratheek J Bhat -  1RV18EC105**\n
            
            """
        )
        st.write("#")
        st.header("Guided by")
        st.write(
            """
            **Rajani Katiyar, Assistant Professor, Electronics and Communication Engineering.** 
            """
        )

    with st.sidebar:
        draw_all("sidebar")

    # model = tf.keras.models.load_model("saved_model/mdl_wts.hdf5")
    json_file = open("saved_model/model-102.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("saved_model/model2.h5")

    # load file
    uploaded_file = st.file_uploader(
        "Upload Your Eye Image Here ", type="jpg")

    map_dict = {0: 'Bulging',
                1: 'Cataract',
                2: 'Crossed',
                3: 'Glaucoma ',
                4: 'Normal eye',
                5: 'Uveitis'
                }

    if uploaded_file is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(opencv_image, (224, 224))

        # Now do something with the image! For example, let's display it:

        col1, col2 = st.beta_columns(2)
        col1.subheader("Original Image ")
        col1.image(resized, use_column_width=True)

        col2.subheader("Grayscale Image")
        grayscale_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(grayscale_image, (224, 224))
        col2.image(resized_gray, use_column_width=True)

        img_reshape = resized[np.newaxis, ...]

        Genrate_pred = st.button("Generate Prediction")
        if Genrate_pred:
            prediction = model.predict(img_reshape).argmax()
            print(prediction)

            st.title("Predicted Label for the image is {}".format(
                map_dict[prediction]))
            print(map_dict[prediction])
