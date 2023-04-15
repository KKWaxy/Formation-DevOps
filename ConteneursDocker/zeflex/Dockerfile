FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* 
    #Good
    #&& python -m pip install -r requirements.txt
# Bad 
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]