FROM python:3.7-slim
COPY /. /backend
WORKDIR /backend

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]