# FROM node:18-alpine3.18 as angular
# WORKDIR /app
# COPY . .
# RUN npm install 
# RUN npm run build

# FROM httpd:alpine3.15
# WORKDIR /usr/local/apache2/htdocs
# COPY --from=angular /app/dist/test .


# FROM node:latest AS builder
# COPY . ./test-a-application
# WORKDIR /test-a-application
# RUN npm i
# RUN npm run build --prod

# FROM nginx:1.15.8-alpine
# COPY --from=builder /test-a-application/dist/test/ /usr/share/nginx/html


FROM node:latest
WORKDIR /app
COPY . .
RUN npm install -g @angular/cli
RUN yarn install
CMD [ "ng","serve","--host","0.0.0.0" ]