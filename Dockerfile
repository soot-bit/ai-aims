FROM python:alpine3.18 
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["/bin/sh", "-c", "python ./main.py"]
