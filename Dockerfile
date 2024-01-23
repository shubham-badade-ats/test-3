# FROM node:18-alpine3.18 as angular
# WORKDIR /app
# COPY . .
# RUN npm install 
# RUN npm run build

# FROM httpd:alpine3.15
# WORKDIR /usr/local/apache2/htdocs
# COPY --from=angular /app/dist/test .
FROM node:latest
WORKDIR /app
COPY . .
RUN npm install -g @angular/cli
RUN yarn install
CMD [ "ng","serve","--host","0.0.0.0" ]