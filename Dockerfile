FROM python:3.8.5

WORKDIR /code
COPY help_files/requirements.txt .
RUN pip install -r requirements.txt
COPY help_files .
CMD flask run -h 0.0.0.0 -p 80
