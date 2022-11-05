FROM python:3.10.5

RUN mkdir /control_user
WORKDIR /control_user
ADD requirements.txt /control_user/
RUN pip install django-uuidfield
RUN pip install -r requirements.txt
ADD . /control_user