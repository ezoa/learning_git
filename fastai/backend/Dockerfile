#FROM python:3.11
FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime

WORKDIR /app

COPY  requirements.txt /app/requirements.txt

COPY . /app

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN apt-get update && apt-get install libgl1


RUN  pip install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn","app:app","--host","0.0.0.0","--reload" ]
