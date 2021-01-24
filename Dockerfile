FROM debian:buster

USER root
RUN apt update
RUN echo '**** Install Python 3.8 *****'
RUN apt-get install -y wget
CMD apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev
CMD apt install -y libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

RUN wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
CMD cd Python-3.8.2
CMD ./configure --enable-optimizations
CMD make altinstall

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

# RUN \
#   echo '**** Setup firefox **** ' \
#   && apt-get remove iceweasel \
#   && apt-get -y install apt-transport-https ca-certificates \
#   && echo '\ndeb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main' | tee -a /etc/apt/sources.list > /dev/null \
#   && apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29 \
#   && apt-get update \
#   && apt-get install firefox-mozilla-build \
#   && apt-get install -y libdbus-glib-1-2 \
#   && apt-get install -y libgtk2.0-0 \
#   && apt-get install -y libasound2

RUN \
  echo '**** Create test directory  **** ' \
  && mkdir /usr/local/test

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

RUN \
  echo '**** Copy gecko & chromedriver ****'

# COPY geckodriver /usr/local/bin
COPY chromedriver /usr/local/bin

RUN \
  echo '**** Copy tests ****'
# COPY gecko_test.py /usr/local/test
# COPY chrome_test_xfvb.py /usr/local/test
# COPY chrome_test.py /usr/local/test
COPY . addressbook

RUN \
  echo 'All went well Done!'
