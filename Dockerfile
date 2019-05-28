FROM python:3.6

WORKDIR /flaskvue

RUN apt-get update
#node.js インストール
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN pip install Flask
RUN npm install -g vue-cli

EXPOSE 8080
