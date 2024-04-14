import streamlit as st

import numpy as np
import os
import requests
from PIL import Image
import io
from io import StringIO


def call_api(file):

    file = {"file": file}
    # st.write(type(file))

    try:

        response = requests.post("http://localhost:8000/run_model", files=file)

        if response.status_code == 200:
            # convert the content byte into pillow
            # response.content
            try:

                processed_image = Image.open(io.BytesIO(response.content))
                st.session_state.processed_image = processed_image

            except Exception as e:
                st.error(f"something wrong happen {e}")

        else:
            st.error(f"connexion is not possible {response.status_code}")

    except Exception as e:

        return


def main():

    st.title("Ezoa test")
    st.sidebar.header("Parameters")

    # Upload video
    image_file = st.sidebar.file_uploader("Upload Images")
    # st.write(image_file)
    if image_file is not None:
        # image_file=image_file.getvalue()
        # st.write(bytes_data)
        st.session_state.image_file = image_file
        # format of image from streamlit is a Bytes io
        # image_uploaded=Image.open(io.BytesIO(image_file))
        # st.image(image_file)

    # Button to run the model
    if st.sidebar.button("Start Tracking"):
        if image_file is not None:

            call_api(image_file)

    col1, col2 = st.columns(2)

    with col1:

        if image_file is not None:
            st.image(image_file, caption="initial image")

    with col2:
        processed_image = st.session_state.get("processed_image", None)

        if processed_image is not None:
            st.image(processed_image, caption="Yolo result")


if __name__ == "__main__":
    main()
