FROM python:3.6
ADD . /app/spider
ADD backend /app/backend
WORKDIR /app/spider
RUN pip3 install -r requirements.txt
CMD python3 run.py