import re
from pathlib import Path 

homedir = Path(__file__ ).parent
json_f_path = homedir.joinpath('yelp').joinpath('yelp_academic_dataset_review.json') 

regex_business_id = re.compile(r'\"business_id\"\:\"(.*?)\"')

with open(json_f_path) as json_f:
    for n, line in enumerate(json_f.readlines()):
        if n < 10:
            found = re.findall(regex_business_id, line)[0]
            print(n, found)
        else:
            exit()