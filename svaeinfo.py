
    '''st.title("Ezoa test")
    st.sidebar.header("Parameters")

    # Upload video
    image_file = st.sidebar.file_uploader("Upload Images")

    # Button to run the model
    if st.sidebar.button("Start Tracking"):


        if image_file:
            
            

            base_path = "/home/ezoa/Documents/learning_git/fastai/"
            image_file_path = os.path.join(base_path, image_file.name)
            fixed_path="/home/ezoa/Documents/learning_git/fastai/results/"
            


        

    
            params = {
                "image_folder_path": image_file_path,
                "output_folder_path": "/home/ezoa/Documents/learning_git/fastai/results/",
                

    
                 

            }
           
            
            response = requests.post("http://localhost:8000/run_model", json=params)
           
            if response.status_code == 200:
                st.text(" Model processing completed.")
                st.image("/home/ezoa/Documents/learning_git/fastai/results/result/image0.jpg")           
                
                
            else:
                st.text(f"No conexion to server: Error - {response.status_code}").'''
        

            