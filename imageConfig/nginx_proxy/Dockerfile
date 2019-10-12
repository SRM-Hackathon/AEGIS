#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - nginx image for proxy configuration

FROM nginx:alpine

COPY index.html /usr/share/nginx/html/

# RUN rm /etc/ngnix/conf.d/*

COPY proxy.conf /etc/ngnix/conf.d/
