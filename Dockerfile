#simple index.html using NGINX
# FROM nginx:latest
# COPY index.html /usr/share/nginx/html/index.html
# EXPOSE 80

#nodejs
FROM node:18
WORKDIR /app
COPY index.js .
CMD ["node", "index.js"]
EXPOSE 80

#python
# FROM python:3.9-slim-buster
# WORKDIR /app
# COPY app.py .
# CMD ["python", "app.py"]
# EXPOSE 80