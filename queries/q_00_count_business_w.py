from SPARQLWrapper import SPARQLWrapper, JSON

def get_boston_b_ids():
    sparql = SPARQLWrapper("http://192.168.60.113/jena/fuseki/yelp_Boston/query")
    sparql.setQuery("""
        SELECT ?b ?bid
        WHERE {
                {
                    ?b a <https://myontology.com#business>;
                        <https://myontology.com#business_id> ?bid .                            
                }
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    business_ids = [result['bid']['value'] for result in results["results"]["bindings"]]
    print(len(business_ids))
    return business_ids

business_ids = get_boston_b_ids()