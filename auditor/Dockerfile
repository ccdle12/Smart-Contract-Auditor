FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python-pip

COPY . /opt/source-code

CMD ["python", "/opt/source-code/tests.py"]
CMD ["python", "/opt/source-code/parse_contract.py"] 
