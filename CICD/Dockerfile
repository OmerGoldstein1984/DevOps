FROM nginx:alpine
COPY index.html /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=3m --timeout=10s CMD curl --fail http://nginx.host.com/ || exit 1
