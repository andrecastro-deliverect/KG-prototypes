from rdflib import Graph, RDF, graph

g = Graph()
qres = g.query(
    """
    SELECT *
    WHERE 
    {
    SERVICE <http://192.168.60.113/jena/fuseki/yelp_Boston/sparql>
        { 
            SELECT ?b ?bid ?p ?v
            WHERE {
                    {
                        ?b a <https://myontology.com#business>;
                           ?p ?v #  <https://myontology.com#business_id> ?bid .                            
                        }
            }
        }
    }
    """
