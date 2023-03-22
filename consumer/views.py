from django.shortcuts import render
from django.http import HttpResponse
from utils.consumer import ConsumerAPI
from django.shortcuts import redirect
from django.core.paginator import Paginator
from pprint import pprint


# Create your views here.
def index(request):
    NUMBER_OF_GAMES = 12
    plataforma = request.GET.get('plataforma')
    categoria = request.GET.get('categoria')
    ordem = request.GET.get('ordem')

    
    if plataforma != '' or categoria != '' or ordem != '':
        
        url = 'https://www.freetogame.com/api/games?'   
        
        if plataforma:
            url += f'platform={plataforma}'
            if categoria:
                url += f'&category={categoria}'
            if ordem:
                url += f'&sort={ordem}'
        
        elif categoria:
            url += f'category={categoria}'
            if ordem:
                url += f'&sort={ordem}'

        elif ordem:
            url += f'sort={ordem}'

        consumer = ConsumerAPI()
        games = consumer.consume(url=url)
        paginator = Paginator(games, NUMBER_OF_GAMES)

        page = request.GET.get('page')
        games_list = paginator.get_page(page)

        return render(request, 'index.html', context={'games': games_list}) 


    consumer = ConsumerAPI()
    games = consumer.consume()
    paginator = Paginator(games, NUMBER_OF_GAMES)
    page = request.GET.get('page')
    games_list = paginator.get_page(page)

    return render(request, 'index.html', context={'games': games_list})

def detalhe(request, id):
    consumer = ConsumerAPI()
    game = consumer.detail_game(id)
    return render(request, 'detalhes.html', context={'game': game})
