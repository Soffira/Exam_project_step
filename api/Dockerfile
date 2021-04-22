FROM python:3.9-alpine
WORKDIR /api
COPY . /api
RUN pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python3"]
CMD ["data.py"]
