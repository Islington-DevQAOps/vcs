FROM php:apache
# COPY index.html /usr/share/nginx/html/index.html
COPY index.php /var/www/html/index.php
EXPOSE 80