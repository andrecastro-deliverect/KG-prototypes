import json
import os
from pathlib import Path
from pprint import pprint
import pandas as pd


homedir = Path(__file__ ).parent
yelpdir = homedir.joinpath('yelp') 

json_f = yelpdir.joinpath('yelp_review.json')
chunks = pd.read_json(json_f, lines=True, chunksize = 100)

for i, chunk in enumerate(chunks):
    if i < 1:
        print(chunk)


# with open(json_f, 'r') as json_f_r:
#     json_content = json.loads(json_f_r.read())

# for n, item in enumerate(json_content):
#     if n < 10:
#         pprint(item)
