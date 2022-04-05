FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY . /app
WORKDIR /app

CMD [ "python3", "src/mindmap.py"]