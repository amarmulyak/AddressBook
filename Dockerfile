FROM ubuntu:18.04
COPY . addressbook
WORKDIR addressbook
RUN apt-get update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update
RUN apt install python3.8 -y
RUN python3.8 --version
RUN apt-get install python3-setuptools -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
CMD pytest -v -n auto --dist loadscope tests/