FROM python:3
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python3"]
CMD ["data.py"]
