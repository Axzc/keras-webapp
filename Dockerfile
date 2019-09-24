FROM python:3.6

COPY . /app
WORKDIR /app
RUN apt-get update -y && apt-get install -y  nfs-common  vim  python3-pip
RUN pip3 install Werkzeug Flask numpy Keras gevent pillow h5py
RUN pip3 install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple


EXPOSE 5000
CMD [ "python" , "app.py"]

