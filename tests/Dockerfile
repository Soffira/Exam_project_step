FROM python:3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
ADD . /tests/
WORKDIR /tests/
ENTRYPOINT ["python3"]
CMD ["tests.py"]
