FROM python:3.11.3-buster

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD [ "python" , "manage.py" , "runserver" , "0.0.0.0:8000"]