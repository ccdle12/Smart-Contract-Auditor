FROM node:latest

LABEL Chris Coverdale <chris.coverdale24@gmail.com>

RUN mkdir /code

WORKDIR /code

RUN npm install -g truffle

# Needs to be install in the local truffle folder
RUN npm install -g mocha
RUN npm install --save-dev chai
RUN npm install chai-as-promised
RUN npm install chai-bignumber



