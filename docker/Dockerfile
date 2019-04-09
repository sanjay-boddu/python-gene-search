FROM python:3.7.3

# maintainer of the image
LABEL maintainer="sboddu@ebi.ac.uk"
# Environment variable
ENV PYTHONUNBUFFERED TRUE

RUN git clone --depth 1 https://github.com/sanjay-boddu/python-gene-search.git /usr/src/gene-search-app

WORKDIR usr/src/gene-search-app

RUN pip3 install --no-cache-dir -r requirements.txt \
    && python dump_genes.py

EXPOSE 8011

CMD ["gunicorn","--bind=0.0.0.0:8011","--access-logfile=/usr/src/gunicorn.access.log","--error-logfile=/usr/src/gunicorn.error.log","app"]
