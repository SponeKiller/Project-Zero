# 1) Build stage
FROM node:23-alpine AS build
WORKDIR /app
COPY app/package*.json ./
RUN npm ci
COPY app .
RUN npm run build 

# 2) Run stage
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html
# Sart application
EXPOSE 80
CMD ["nginx","-g","daemon off;"]
