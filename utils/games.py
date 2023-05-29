import requests
import json

class Games:
    def __init__(self) -> None:
        self.__url_all_games = 'https://www.freetogame.com/api/games'
        self.__url_game = 'https://www.freetogame.com/api/game?id='

    def get_all_games(self):
        """ Retorna todos os jogos da API """
        return json.loads(requests.get(self.__url_all_games).content)
    
    def get_game(self, id:int):
        """ Retorna todos os detalhes de um jogo usando id:int na pesquisa """
        return json.loads(
            requests.get( self.__url_game + str(id) ).content
        )
    
    def get_games_filter(self, platform=None, category=None, sort=None):
        """ Retorna todos os games que correspondem aos filtros passados como argumento do método"""
        url = self.__url_all_games
        if platform:
            url += f"?platform={platform}"

            if category:
                url += f"&category={category}"
            
            if sort:
                url += f"&sort={sort}"
        
        elif category:
            url += f"?category={category}"

            if sort:
                url += f"&sort={sort}"
        
        elif sort:
            url += f"&sort={sort}"

        return json.loads(
            requests.get(url).content
        )