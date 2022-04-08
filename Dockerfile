FROM python:3.10-slim
WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY config config
COPY database database
COPY logger logger
COPY bot bot
COPY routes routes
COPY ui/public ui
COPY main.py .
CMD [ "uvicorn", "main:app", "--reload", "--use-colors", "--host", "0.0.0.0", "--port", "105" ]
