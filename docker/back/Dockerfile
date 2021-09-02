FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD ./src/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt