FROM python:3.10

WORKDIR /app

COPY  requirements.txt .

RUN pip install -r requirements.txt

COPY  . /app


EXPOSE 8501

ENTRYPOINT [ "streamlit","run", "app.py" ]
