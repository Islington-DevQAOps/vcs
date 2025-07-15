#simple index.html using NGINX
FROM nginx:latest
# COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80

#nodejs
FROM node:lts-alpine
WORKDIR /app
COPY index.js .
CMD ["node", "index.js"]
EXPOSE 3000