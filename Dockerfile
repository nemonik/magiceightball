FROM python:2.7
MAINTAINER Michael Joseph Walsh <mjwalsh@mitre.org>
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","magiceightball.py"]
