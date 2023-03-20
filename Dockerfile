FROM python:3.9-slim-buster
WORKDIR /flask-weather
COPY . .
RUN pip install -r requirements.txt
CMD [ "flask", "--app", "server", "run", "--host=0.0.0.0" ]