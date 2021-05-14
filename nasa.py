#!/usr/bin/python3
import requests
import argparse
import math
import json
import csv

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

version = "1.0.0"

introduction = """This is a script that receives an argument and queries
               the api ('https://images-api.nasa.gov/search') with the argument as the query string.
               If no argument is passed, the default query string is 'Ilan Ramon' """

parser = argparse.ArgumentParser(description=introduction, formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=27))
parser.add_argument("-v", "--version", help="show program version", action="store_true")
parser.add_argument("-q", "--query", help='set query text, use double or single quotes for queries with whitespace,for example: "Ilan Ramon"', default="Ilan Ramon")
args = parser.parse_args()

if args.version:
    print("This is nasa-api-script version {}".format(version))
if args.query:
    print("Set query text to {}".format(args.query))

params = {"q": args.query, "media_type": "image"}
try:
    r = requests.get('https://images-api.nasa.gov/search', params=params)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

jsonObject = json.loads(r.text)

with open('/app/csv_files/%s-nasa-api.csv' % args.query.strip().replace(" ", "-"), mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["file_name", "Size", "url"])
    for item in jsonObject["collection"]["items"]:
        img_size = requests.get(item["links"][0]["href"]).content
        print("too small: {}".format(item["links"][0]["href"].rsplit('/',1)[1]))
        if int(len(img_size)) >= 71680:
            print("file_name: {} size: {} url: {}".format(item["links"][0]["href"].rsplit('/',1)[1], convert_size(len(img_size)), item["links"][0]["href"]))
            writer.writerow([item["links"][0]["href"].rsplit('/',1)[1], convert_size(len(img_size)), item["links"][0]["href"]])
