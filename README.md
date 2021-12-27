# Knowledge Graph Prototype

## Jupyter Notebook

**SPARQL Queries to Yelp Businesses and Reviews in Boston [Exploring_yelp_data.ipynb](./Exploring_yelp_data.ipynb)**
## Yelp Restaurants and reviews in Boston

From [Yelp Open Dataset](https://www.yelp.com/dataset):
* a subsection of the Business and Review datasets were extracted
* concerning businesses in Boston

The subsection of the data was
* converted from JSON to RDF using [JSON2RDF](https://github.com/AtomGraph/JSON2RDF) and mapped to made-up ontology URI `https://myontology.com#` 
    * run: `cat yelp/yelp_review.json|docker run -i -a stdin -a stdout -a stderr atomgraph/json2rdf https://localhost/`
`cat yelp/yelp_review.json|docker run -i -a stdin -a stdout -a stderr atomgraph/json2rdf https://localhost/ | riot --syntax=n3 --out=ttl`
* written to the [Apache Jena Fuseki
](https://jena.apache.org/documentation/fuseki2/) triple store  as triples

In [json2rdf_graph_reviews_Boston.py](./json2rdf_graph_reviews_Boston.py) and [json2rdf_graph_business_Boston.py](./json2rdf_graph_business_Boston.py)
