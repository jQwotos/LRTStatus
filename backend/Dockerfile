FROM python:3

EXPOSE 5000/udp

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "./src/server.py" ]