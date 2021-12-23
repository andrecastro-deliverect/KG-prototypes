import re
import subprocess
from pathlib import Path
from pprint import pprint
from rdflib import Graph, RDF, graph
import requests


homedir = Path(__file__ ).parent
yelpdir = homedir.joinpath('yelp') 

yelpdir_files = {
    #'review': 'yelp_academic_dataset_review.json',
    'business': 'yelp_academic_dataset_business.json'
} 
large_graph = Graph()

for rdfclass, json_f in yelpdir_files.items():
    json_f_path = yelpdir.joinpath(json_f)
    json_out_f_path = yelpdir.joinpath('1entry.json')
    print(json_out_f_path)
    with open(json_f_path) as json_f:
        for n, line in enumerate(json_f.readlines()):
            if n > 860:
                # write to tmp file
                with open(json_out_f_path, 'w') as json_out_f:
                    json_out_f.write(line)
                command = f'cat {json_out_f_path} | docker run -i -a stdin -a stdout -a stderr atomgraph/json2rdf https://myontology.com | riot --syntax=n3 --out=ttl'
                n3_output = subprocess.check_output(command, shell=True) # stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                oneitem_graph = Graph()
                oneitem_graph.parse(n3_output)
                insert_query = '''INSERT { ?subject a <https://myontology.com#%s> } WHERE { ?subject ?predicate ?object . }''' % rdfclass
                oneitem_graph.update(insert_query)
                large_graph = large_graph + oneitem_graph
                if n % 10 == 0:

                    graph_ttl = large_graph.serialize(format='turtle')
                    try:
                        # insert to graph in triple-store
                        headers = {'Content-Type': 'text/turtle;charset=utf-8'}
                        r = requests.post('http://192.168.60.113/jena/fuseki/yeld_b_r/data?default', data=graph_ttl, headers=headers)
                        print(r.status_code)
                    except:
                        print('failed request')

                    large_graph = Graph() # reset large


