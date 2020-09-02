FROM python:3

ENV APP_NAME=${APP_NAME}

ARG HOME="/app"
ENV HOME=${HOME}

WORKDIR ${HOME}

ADD requirements.txt requirements.txt
ADD . ${HOME}/${APP_NAME}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e ${HOME}/${APP_NAME}