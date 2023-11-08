FROM python:3.9

EXPOSE 8000

ARG ENV
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

#RUN apt-get update && apt-get install -y
#
## Install Postgres Client and Server
#RUN apt-get install postgresql-client -y
#RUN apt-get install -y build-essential postgresql-server-dev-all

# Upgrade pip
#RUN pip install --no-cache-dir --upgrade pip


#CMD ["python", "manage.py", "makemigrations"]
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




