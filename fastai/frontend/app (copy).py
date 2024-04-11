import streamlit as st

import numpy as np
import os
import requests
from PIL import Image
import io


def process_image(uploaded_file):
    st.write(uploaded_file)

    if uploaded_file is not None:

        with st.spinner("Process image  ..."):

            files= {"file ": uploaded_file.getvalue()}
            response= requests.post("http://localhost:8000/run_model/",files =files)
            if response.status_code==200:
                try:

                    processed_image=Image.open(io.BytesIO(response.content))
                    st.session_state.processed_image=processed_image
                except Exception as e:
                    st.error(f"Error processing image : {e}")
            else:
                st.error(f"Failed to proceed image  status code : {response.status_code}")





def main():
    st.set_page_config(

        page_title="Object recognition",
        layout="wide",
        initial_sidebar_state="expanded"




    )


    st.title("Object recognition")
    uploaded_image= st.session_state.get(" uploaded_image",None)
    image_file = st.sidebar.file_uploader("Upload Images")




    if image_file is not None:

        uploaded_image= Image.open(image_file)
        st.session_state.uploaded_image=uploaded_image
        st.write(type())
        if st.sidebar.button("Start Tracking"):
            process_image(image_file)


    
    #Main content area 

    col1,col2 = st.columns(2)


    with col1:
        if uploaded_image is not None:
            st.subheader("Original Image")
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    with col2:
        processed_image = st.session_state.get("processed_image", None)
        if processed_image is not None:
            st.subheader("Processed Image")
            st.image(processed_image, caption="Processed Image", use_column_width=True)












            
if __name__ == "__main__":
   main()