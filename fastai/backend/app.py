from typing import Union
from fastapi import FastAPI, Response, requests, UploadFile, File


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

app = FastAPI()


def process_image(img):

    img = Image.open(io.BytesIO(img))

    model = yolov5.load("model/yolov5s.pt")

    try:

        results = model(img)
        results.ims

        results.render()

        base64_images = []
        for im in results.ims:
            buffered = BytesIO()
            im_based64 = Image.fromarray(im)
            im_based64.save(buffered, format="JPEG")

            base64_images.append(base64.b64encode(buffered.getvalue()).decode("utf-8"))
        return im_based64

    except Exception as e:
        return []


@app.post("/run_model")
async def run_model(file: UploadFile = File(...)):
    content = await file.read()
    processed_image = process_image(content)

    if processed_image is not None:

        output_image = io.BytesIO()
        processed_image.save(output_image, format="JPEG")
        processed_image.save("output image.jpg", "JPEG")
        print(type(output_image))

        return Response(content=output_image.getvalue(), media_type="image/jpeg")
    else:
        return {"message": "model process bad"}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
