from amazon.api import AmazonAPI
from config import AWS_KEY, SECRET_KEY, ASSOCIATE_KEY

from flask import Flask, url_for
from flask import request
from flask import jsonify
from flask import Response

import collections
import json

amazon = AmazonAPI(AWS_KEY, SECRET_KEY, ASSOCIATE_KEY)

app = Flask(__name__)

@app.route('/search')
def api_results():
    if 'q' in request.args:
        return search_products(request.args['q'], 'Video')
    else:
        return search_products('topgun', 'Video')

def search_products(query, index):

    products = amazon.search_n(10, Keywords=query, SearchIndex=index)

    data = []
    for i, product in enumerate(products):
        item = collections.OrderedDict()
        item['counter'] = i
        item['product_title'] = product.title
        item['product_url'] = product.offer_url
        item['product_price'] = product.list_price
        item['product_image_medium'] = product.medium_image_url
        item['product_image_large'] = product.large_image_url
        data.append(item)

    output = json.dumps(data)
    jsonp_output = 'azinstant({"query": "' +  query + '", "products":' + output + '});'

    resp = Response(jsonp_output, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(debug=True)