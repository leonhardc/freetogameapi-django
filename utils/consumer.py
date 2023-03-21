from pprint import pprint
import requests
import json


class ConsumerAPI:
    def __init__(self) -> None:
        self.url = 'https://www.freetogame.com/api/games'

    def consume(self, url=None):
        if url: 
            request = json.loads(requests.get(url).content)    
        else: 
            request = json.loads(requests.get(self.url).content)
        return request

if __name__== '__main__':
    consumer = ConsumerAPI()
    consumer.consume()