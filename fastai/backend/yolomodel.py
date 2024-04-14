
from datetime import datetime
from io import BytesIO
from PIL import Image
import torch
import cv2
import base64
import numpy as np
import yolov5
import os

#app=FastAPI()


#load Yolov5  model

model = yolov5.load('yolov5s.pt')


def process_image(image_path):
    '''
    input : image path with the image 
    output: image, bonding boxes cordinate 


    
    
    '''

    try :
        img= cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        #apply the model 

        results= model(img)
        #results 

   
        #apply the model 

        results= model(img)
        results.ims
        print(type(results.render()))
      
        base64_images=[]
        for im in results.ims:
            print(type(im))
            buffered = BytesIO()
            im_based64= Image.fromarray(im)
            im_based64.save(buffered,format="JPEG")

            base64_images.append(base64.b64encode(buffered.getvalue()).decode('utf-8'))
            return print((base64_images))
        
        ''' predictions = results.pred[0]
        boxes= predictions[:,:4]
        scores= predictions[:,4]
        categories= predictions[:,5]


        # save results into folder
       
        return results.save(save_dir='/home/ezoa/Documents/learning_git/fastai/results/resu')

        
      
       # print(results.save(save_dir='/home/ezoa/Documents/learning_git/fastai/results/',))
        results.render()
        base64_images=[]
        print (results.ims) 
        
        for im in results.ims:

            buffered = BytesIO()
            im_base64= Image.fromarray(im)
            im_base64.save(buffered,format="JPEG")
            base64_images.append(base64.b64encode(buffered.getvalue().decode('utf-8')))
            

        


        return base64_images'''

            






       








    except Exception as e:
        return []
    


    

if __name__=='__main__' :
    upload_counter=0
    image_path ="/home/ezoa/Documents/learning_git/fastai/car.jpeg"
    process_image(image_path)
    
   

    