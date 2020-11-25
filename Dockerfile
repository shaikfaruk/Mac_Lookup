FROM python:3

COPY requirements.txt ./
COPY rest_api.py ./

ADD rest_api.py ./

RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python","./rest_api.py"]
