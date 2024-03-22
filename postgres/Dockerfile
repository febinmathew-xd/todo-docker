FROM postgres:latest

COPY backup.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=todo
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASS=area51