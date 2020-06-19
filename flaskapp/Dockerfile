FROM python:3.8.3

WORKDIR /user/src/app

COPY 'requirements.txt' . 

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]

