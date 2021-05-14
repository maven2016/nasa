# nasa api

Pbulic image available: maven2016/nasa:1.0.0<\br>
Dockerfile included in git as well.<\br>
<\br>
It's possible to execute the nasa.py directly or via docker.<\br>
<\br>
If you run locally make sure you have python 3 installed and in PATH, also make sure to install requests module (pip3 install requests).<\br>
./nasa.py -q "my query"<\br>
For additonal instructions use ./nasa.py --help<\br>
<\br>
To run the script via docker, execute the following command:
docker run -it -v <Full Path to File>/nasa.py:/app/nasa.py -v <Full Path to Folder>/csv_files:/app/csv_files maven2016/nasa:1.0.0 ./nasa.py -q "Ilan Ramon"<\br>
Make sure to replace <Full Path to File> and <Full Path to Folder> with your actual path.<\br>
<\br>
# Optional
To create your own docker image you can execute the following command:<\br>
docker build -t <your tag> . <\br>

if you prefer not mount the nasa.py script every time you may modify the Dockerfile to include it:<\br>
FROM alpine:3.13<\br>
<\br>
WORKDIR /app<\br>
<\br>
RUN apk add --no-cache python3 \<\br>
    && ln -sf python3 /usr/bin/python \<\br>
    && python3 -m ensurepip \<\br>
    && pip3 install --no-cache --upgrade pip requests<\br>
<\br>
COPY ./nasa.py /app/nasa.py  <\br>
<\br>
RUN chmod +x nasa.py <\br>
<\br>
CMD ["./nasa.py"]
