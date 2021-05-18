# nasa api

Public image available: maven2016/nasa:1.0.0</br>
Dockerfile included in git as well.</br>
</br>
It's possible to execute the nasa.py directly or via docker.</br>
</br>
If you run locally make sure you have python 3 installed and in PATH, also make sure to install requests module (pip3 install requests).</br>
Make sure you have a folder in path: /app/csv_files , or modify the script (nasa.py) on line 41: </br>
with open('/app/csv_files/%s-nasa-api.csv'.....</br>
Change to: </br>
with open('%s-nasa-api.csv'..... and the file will created in your workdir.</br>
To execute the script run: </br>
./nasa.py -q "my query"</br>
For additonal instructions use ./nasa.py --help</br>
</br>
To run the script via docker, execute the following command:</br>
docker run -it -v \<Full Path to File\>/nasa.py:/app/nasa.py -v \<Full Path to Folder\>/csv_files:/app/csv_files maven2016/nasa:1.0.0 ./nasa.py -q "apolo 11"</br>
Make sure to replace \<Full Path to File\> and \<Full Path to Folder\> with your actual path.</br>
</br>
# Optional
To create your own docker image you can execute the following command:</br>
docker build -t \<your tag\> . </br>
</br>
if you prefer not mount the nasa.py script every time, you may modify the Dockerfile to include it:</br>
FROM alpine:3.13</br>
</br>
WORKDIR /app</br>
</br>
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python && python3 -m ensurepip && pip3 install --no-cache --upgrade pip requests</br>
</br>
COPY ./nasa.py /app/nasa.py  </br>
</br>
RUN chmod +x nasa.py </br>
</br>
ENTRYPOINT ["./nasa.py"]
</br>
</br>
Now you can execute docker using this command instead:</br>
docker run -it -v \<Full Path to Folder\>/csv_files:/app/csv_files <your docker image:tag> -q "apolo 11"
