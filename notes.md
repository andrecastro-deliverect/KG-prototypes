Using [Yelp open data set](https://www.yelp.com/dataset) (4.9Gb) for Data

Data set contains:
* Reviews
* Restaurants

# JSON2RDF
https://github.com/AtomGraph/JSON2RDF

run: `cat yelp/yelp_review.json|docker run -i -a stdin -a stdout -a stderr atomgraph/json2rdf https://localhost/`
`cat yelp/yelp_review.json|docker run -i -a stdin -a stdout -a stderr atomgraph/json2rdf https://localhost/ | riot --syntax=n3 --out=ttl`

# requirements
* [JSON2RDF](https://github.com/AtomGraph/JSON2RDF) - [docker image](https://hub.docker.com/r/atomgraph/json2rdf) 
        * `docker pull atomgraph/json2rdf`
* [apache jena](https://jena.apache.org/download/index.cgi) - [setting up](https://jena.apache.org/documentation/tools/)


# Sample Data from YELP
yelp_academic_dataset_checkin.json

```json
{'business_id': '--0r8K_AQ4FZfLsX3ZYRDA', 'date': '2017-09-03 17:13:59'}
```

yelp_academic_dataset_tip.json

```json
{'business_id': 'ENwBByjpoa5Gg7tKgxqwLg',
 'compliment_count': 0,
 'date': '2011-07-22 19:07:35',
 'text': 'Carne asada chips...',
 'user_id': 'WCjg0jdHXMlwbqS9tZUx8Q'}
 ```
 
yelp_academic_dataset_review.json

```json
{'business_id': 'buF9druCkbuXLX526sGELQ',
 'cool': 1,
 'date': '2014-10-11 03:34:02',
 'funny': 1,
 'review_id': 'lWC-xP3rd6obsecCYsGZRg',
 'stars': 4.0,
 'text': 'Apparently Prides Osteria had a rough summer as evidenced by the '
         'almost empty dining room at 6:30 on a Friday night. However new '
         'blood in the kitchen seems to have revitalized the food from other '
         'customers recent visits. Waitstaff was warm but unobtrusive. By 8 pm '
         'or so when we left the bar was full and the dining room was much '
         'more lively than it had been. Perhaps Beverly residents prefer a '
         'later seating. \n'
         '\n'
         'After reading the mixed reviews of late I was a little tentative '
         'over our choice but luckily there was nothing to worry about in the '
         'food department. We started with the fried dough, burrata and '
         "prosciutto which were all lovely. Then although they don't offer "
         'half portions of pasta we each ordered the entree size and split '
         'them. We chose the tagliatelle bolognese and a four cheese filled '
         'pasta in a creamy sauce with bacon, asparagus and grana frita. Both '
         'were very good. We split a secondi which was the special Berkshire '
         'pork secreto, which was described as a pork skirt steak with garlic '
         'potato pur??e and romanesco broccoli (incorrectly described as a '
         'romanesco sauce). Some tables received bread before the meal but for '
         'some reason we did not. \n'
         '\n'
         'Management also seems capable for when the tenants in the apartment '
         'above began playing basketball she intervened and also comped the '
         'tables a dessert. We ordered the apple dumpling with gelato and it '
         'was also quite tasty. Portions are not huge which I particularly '
         'like because I prefer to order courses. If you are someone who '
         'orders just a meal you may leave hungry depending on you appetite. '
         'Dining room was mostly younger crowd while the bar was definitely '
         'the over 40 set. Would recommend that the naysayers return to see '
         "the improvement although I personally don't know the former glory to "
         'be able to compare. Easy access to downtown Salem without the crowds '
         'on this month of October.',
 'useful': 3,
 'user_id': 'ak0TdVmGKo4pwqdJSTLwWw'}
 ```

yelp_academic_dataset_business.json

```json
{'address': '921 Pearl St',
 'attributes': {'Alcohol': "'beer_and_wine'",
                'Ambience': "{'touristy': False, 'hipster': False, 'romantic': "
                            "False, 'divey': False, 'intimate': False, "
                            "'trendy': False, 'upscale': False, 'classy': "
                            "False, 'casual': True}",
                'BikeParking': 'True',
                'BusinessAcceptsBitcoin': 'False',
                'BusinessAcceptsCreditCards': 'True',
                'BusinessParking': "{'garage': False, 'street': True, "
                                   "'validated': False, 'lot': False, 'valet': "
                                   'False}',
                'Caters': 'True',
                'DogsAllowed': 'False',
                'GoodForMeal': "{'dessert': False, 'latenight': False, "
                               "'lunch': False, 'dinner': False, 'brunch': "
                               "False, 'breakfast': False}",
                'HappyHour': 'True',
                'HasTV': 'True',
                'NoiseLevel': "u'average'",
                'OutdoorSeating': 'True',
                'RestaurantsAttire': "'casual'",
                'RestaurantsDelivery': 'None',
                'RestaurantsGoodForGroups': 'True',
                'RestaurantsPriceRange2': '2',
                'RestaurantsReservations': 'False',
                'RestaurantsTableService': 'True',
                'RestaurantsTakeOut': 'True',
                'WheelchairAccessible': 'True',
                'WiFi': "u'free'"},
 'business_id': '6iYb2HFDywm3zjuRg0shjw',
 'categories': 'Gastropubs, Food, Beer Gardens, Restaurants, Bars, American '
               '(Traditional), Beer Bar, Nightlife, Breweries',
 'city': 'Boulder',
 'hours': {'Friday': '11:0-23:0',
           'Monday': '11:0-23:0',
           'Saturday': '11:0-23:0',
           'Sunday': '11:0-23:0',
           'Thursday': '11:0-23:0',
           'Tuesday': '11:0-23:0',
           'Wednesday': '11:0-23:0'},
 'is_open': 1,
 'latitude': 40.0175444,
 'longitude': -105.2833481,
 'name': 'Oskar Blues Taproom',
 'postal_code': '80302',
 'review_count': 86,
 'stars': 4.0,
 'state': 'CO'}
``` 




# Neo4j

docker run \
    --name testneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/test \
    neo4j:latest