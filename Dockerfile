FROM debian:buster

USER root

RUN apt update
RUN echo '**** Install Python 3.8 *****'
RUN apt-get install -y wget
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev
RUN apt install -y libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

RUN wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
CMD cd Python-3.8.2/
CMD ./configure --enable-optimizations
CMD make altinstall

COPY . addressbook
WORKDIR addressbook

RUN \
  apt update \
  && echo '**** Set up python **** ' \
  && apt-get install -y python3-dev python-distribute python3-pip \
  && pip3 install pyvirtualdisplay \
  && pip3 install xvfbwrapper \
  && echo '**** Set up selenium, pytest **** ' \
  && pip3 install -U selenium \
  && pip3 install -U pytest \
  && echo 'Setting up xvfb ...' \
  && apt-get -y install xvfb

RUN \
  apt-get install -y unzip libxi6 libgconf-2-4

RUN \
  echo '**** Install chrome     **** ' \
  && apt -y --fix-broken install \
  && apt-get -y install libxss1 libappindicator1 libindicator7 \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && dpkg -i google-chrome*.deb; exit 0

RUN apt-get -y install -f && \
  apt-get -y install unzip

CMD chmod +x chromedriver

RUN pip3 install -r /addressbook/requirements.txt

RUN \
  echo 'All went well Done! Executing tests'

CMD pytest /addressbook/new_test_suite/test_home_page_header.py
