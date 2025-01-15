FROM httpd:latest
RUN apt update && apt upgrade -y
COPY ./templates /var/www/html/
# Copy apache vhost file to proxy php requests to php-fpm container
COPY demo.apache.conf /usr/local/apache2/conf/demo.apache.conf
RUN echo "Include /usr/local/apache2/conf/demo.apache.conf" \
    >> /usr/local/apache2/conf/httpd.conf
RUN chmod -R 755 /var/www/html && chown -R www-data:www-data /var/www/html
#COPY Copiamos la carpeta var/www/html
