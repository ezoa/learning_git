from  typing import Union
from fastapi import FastAPI


from pydantic import BaseModel
from typing import List
import uvicorn



from datetime import datetime
from io import BytesIO
from PIL import Image
import torch
import cv2
import base64
import numpy as np
import yolov5
import os
import io

app=FastAPI()



    

class ImagesParams(BaseModel):
    image_folder_path: str
    output_folder_path: str





def process_image(params: ImagesParams):

    model = yolov5.load('yolov5s.pt')

    try :
        img= cv2.imread(params.image_folder_path, cv2.IMREAD_UNCHANGED)
        #apply the model 

        results= model(img)
        results.ims
        results.render()
        predictions = results.pred[0]
        boxes= predictions[:,:4]
        scores= predictions[:,4]
        categories= predictions[:,5]

        for im in results.ims:
            buffered = BytesIO()
            im_based64= Image.fromarray(im)
            im_based64.save(buffered,format="JPEG")

            base64.b64encode(buffered.getvalue()).decode('utf-8')
            return buffered.getvalue()

        # save results into folder
    
        #return results.save(save_dir='/home/ezoa/Documents/learning_git/fastai/results/result')
        #return results.imgs
     

        



    except Exception as e:
        return []
    

@app.post("/run_model")    
def run_model(params: ImagesParams):
    process_image(params)
    return {"message": "model process well"}


if __name__ == "__main__": 

    uvicorn.run(app, host="0.0.0.0", port=8000)