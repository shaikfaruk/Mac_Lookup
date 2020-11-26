FROM python:3

COPY requirements.txt ./
COPY rest_api.py ./
COPY config.ini ./
ADD rest_api.py ./
ADD config.ini ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python","./rest_api.py"]
