FROM python:3.6

COPY . /app
WORKDIR /app
RUN apt-get update -y && apt-get install -y  nfs-common  vim  python3-pip
RUN pip3 install Werkzeug Flask numpy Keras gevent pillow h5py tensorflow


EXPOSE 5000
CMD [ "python" , "app.py"]

