FROM ubuntu

RUN apt-get update
RUN npm install -g yarn
RUN apt-get install -y python3 python-pip \
    && yarn global add \
        --global-folder /usr/local/share \
          ethereumjs-testrpc \
          truffle \
          truffle-flattener \
          solium \
	      jshint 


COPY . /opt/source-code

CMD ["testrpc", "/opt/source-code/."]
