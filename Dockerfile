FROM python:3.12-alpine

COPY requirements.txt /temp/requirements.txt
COPY NewsPortal_SF_Proj /NewsPortal_SF_Proj
WORKDIR /NewsPortal_SF_Proj
EXPOSE 8000

RUN python -m pip install --upgrade pip

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password news-user

USER news-user
