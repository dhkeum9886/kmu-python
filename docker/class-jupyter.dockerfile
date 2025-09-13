FROM jupyter/base-notebook:python-3.9.12
RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
WORKDIR /home/jovyan/work