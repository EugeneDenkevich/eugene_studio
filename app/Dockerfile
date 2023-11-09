FROM python:3.11-bullseye

WORKDIR /blog

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools wheel

COPY ./requirements.txt ./app/requirements.txt
RUN pip install -r /blog/app/requirements.txt

COPY . /blog/app

EXPOSE 8000

RUN chmod +x ./app/entrypoint.sh
ENTRYPOINT ["./app/entrypoint.sh"]
