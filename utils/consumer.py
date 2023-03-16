from pprint import pprint
import requests
import json


class Consumer:
    def __init__(self) -> None:
        self.url = 'https://www.freetogame.com/api/games'

    def consume(self, filter=None):
        request = requests.get(self.url)
        request = json.loads(request.content)
        for game in request:
            pprint(game)
            break

if __name__== '__main__':
    consumer = Consumer()
    consumer.consume()