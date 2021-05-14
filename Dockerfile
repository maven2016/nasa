FROM alpine:3.13

WORKDIR /app

RUN apk add --no-cache python3 \
    && ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip requests

CMD ["python"]
