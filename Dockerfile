ARG OUT_DIR
FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py", "--out-dir", $OUT_DIR ]