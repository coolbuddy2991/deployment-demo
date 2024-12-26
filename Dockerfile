FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn","-b","0.0.0.0:5000","app:app","--reload"]



