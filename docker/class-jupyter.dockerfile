FROM jupyter/base-notebook:python-3.9.12

WORKDIR /opt/app
COPY requirements.txt /opt/app/requirements.txt

RUN python -m pip install --upgrade pip wheel \
 && python -m pip install 'setuptools<75' \
 && python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /home/jovyan/work
