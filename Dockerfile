FROM python:3.10
RUN apt-get update
RUN apt-get upgrade -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN mv /etc/localtime /etc/localtime.old
RUN ln -s /usr/share/zoneinfo/Europe/Madrid /etc/localtime
COPY ./src /app/src
COPY ./config /app/config
ENV CONFIG_PATH="/app/config/"
COPY ./envs /app/envs
COPY ./.env /app/.env
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app/src
RUN useradd uapplda -u 1023 --create-home --user-group
RUN chown -R uapplda:uapplda /app
RUN mkdir -p /var/log/uvicorn/
RUN touch /var/log/uvicorn/access.log
RUN touch /var/log/uvicorn/error.log
USER 1023
EXPOSE 5001/tcp
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001", "--log-level", "info"]