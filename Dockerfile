FROM python:3.9.17-bullseye 

RUN pip install --upgrade pip

COPY . /opt/test-ghactions
WORKDIR /opt/test-ghactions
RUN pip install -r requirements.txt

WORKDIR /opt/test-ghactions
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--preload", "-w", "4", "main:app"]

EXPOSE 8000

