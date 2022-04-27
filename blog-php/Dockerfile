FROM sunasteriskrnd/php:7.4-nginx-alpine
COPY --chown=www-data:www-data data/ /var/www/html/
COPY ./default.conf /etc/nginx/templates.d/
COPY ./secret_flag /tmp/
RUN chown www-data:www-data -R /var/www/html/
ENV DOCUMENT_ROOT=/var/www/html/
RUN wget -O /usr/local/bin/deadline https://gist.githubusercontent.com/thphuong/bdb5b93f67f4420a2522cc59a257b8b4/raw/c2a846091645b2402d5a96b51ae9d923fb6df118/deadline.sh \
    && chmod +x /usr/local/bin/deadline

HEALTHCHECK --interval=1m --timeout=1s CMD deadline 43200

