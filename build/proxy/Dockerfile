FROM nginx

RUN mkdir -p /var/www/media \
    && mkdir -p /var/www/static \
    && mkdir -p /var/www/django_admin/static 


RUN chown -R nginx:nginx /var/www/media \
    && chown -R nginx:nginx /var/www/static \
    && chown -R nginx:nginx /var/www/django_admin/static 

VOLUME [ "/etc/nginx/" ]