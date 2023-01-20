FROM ubuntu
RUN apt-get update
RUN apt install -y  python3
RUN mkdir lab1
WORKDIR lab1
COPY myserv.py .
COPY myclient.py .
CMD ["python3","myserv.py" ]
