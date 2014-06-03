import json

from amazon.api import AmazonAPI
import collections

amazon = AmazonAPI('foo1', 'foo2', 'foo')

def search_products():
    # pass keyword
    # searchIndex = get as an option, else search all

    # data = []
    products = amazon.search_n(10, Keywords='nike', SearchIndex='All')
    # for i, product in enumerate(products):
    #     item = (product.title, product.offer_url, product.medium_image_url, product.large_image_url)
    #     data.append(item)

    # print json.dumps(data)

    data = []
    for i, product in enumerate(products):
        item = collections.OrderedDict()
        item['counter'] = i
        item['product_title'] = product.title
        item['product_url'] = product.offer_url
        item['product_image_medium'] = product.medium_image_url
        item['product_image_large'] = product.large_image_url
        data.append(item)

    print products
    print products.__dict__    
    # print json.dumps(data)

search_products()
