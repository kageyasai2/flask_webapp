FROM python:3.6

WORKDIR /myapp
ADD requirements.txt /myapp

RUN apt-get update
#node.js インストール
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN pip install Flask
RUN pip install -r requirements.txt
RUN npm install -g @vue/cli