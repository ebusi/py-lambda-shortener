from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event))

    routes = []
    with open("urls.json") as file:
        routes = json.loads(file.read())

    proxy = event['pathParameters']['proxy']
    
    redirect_route = list(filter(lambda route: route["key"] == proxy, routes))
    
    if len(redirect_route) == 1:
        return {
            "statusCode": 301,
            "headers": {
                "Location": redirect_route[0]["url"]
                }
            }
