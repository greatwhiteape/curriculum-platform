FROM python:3.7.0

# Output logging faster
ENV PYTHONUNBUFFERED 1
# Don't write bytecode
ENV PYTHONDONTWRITEBYTECODE 1

# geodjango spatial requirements
# RUN apt-get update && apt-get install -y \
#     binutils

# Working directory
RUN mkdir /app
WORKDIR /app

# App requirements

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt \
    && groupadd uwsgi && useradd -g uwsgi uwsgi

# Copy app to working directory
COPY ./ /app/

RUN chown -R uwsgi:uwsgi /app

WORKDIR /app

ENTRYPOINT ["/app/utils/entrypoint.sh"]

CMD ["uwsgi", "--http", ":8080", "--wsgi-file", "curriculum_platform/wsgi.py", "--master", "--processes", "4", "--threads", "2", "--uid", "uwsgi", "--gid", "uwsgi"]
