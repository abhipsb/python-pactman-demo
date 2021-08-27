FROM       python:3.7.9-alpine3.11

WORKDIR /home
COPY . .
RUN chmod 755 -R .
RUN apk update
RUN apk upgrade
RUN apk add gcc py-pip python-dev libffi-dev openssl-dev gcc libc-dev bash make
RUN python -m pip install --upgrade pip
RUN python -m pip install psutil
RUN pip install -r requirements.txt
CMD ./docker-start.sh