FROM ultralytics/ultralytics:8.1.1

COPY  requirements.txt /app/requirements.txt

WORKDIR /app


COPY . /app


RUN  pip install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn","app:app","--host","0.0.0.0","--port","8000","--reload" ]
