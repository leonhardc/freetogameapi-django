from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.consumer import ConsumerAPI
from django.shortcuts import redirect
from django.core.paginator import Paginator
from pprint import pprint


def index(request):
    NUMBER_OF_GAMES = 12
    plataforma = request.GET.get('plataforma')
    categoria = request.GET.get('categoria')
    ordem = request.GET.get('ordem')
    pesquisa = request.GET.get('search')

    # Iniciando o Objeto Session
    if not request.session.get('games_salvos'):
        request.session['games_salvos'] = []
        request.session.save()

    # Se existe algum termo no formulario de pesquisa
    if pesquisa != None:
            
        consumer = ConsumerAPI()
        games = consumer.consume()
        filter = []

        for game in games:
            if pesquisa.lower() in game['title'].lower() or \
                pesquisa.lower() in game['short_description'].lower() or \
                pesquisa.lower() in game['genre'].lower():
                filter.append(game)

        games = filter
        paginator = Paginator(games, NUMBER_OF_GAMES) # Paginação
        page = request.GET.get('page')
        games_list = paginator.get_page(page)
        return render(request, 'index.html', context={'games': games_list}) 

    
    # Se existe alguma plataforma, categoria ou ordem pesquisada
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

def saveGame(request, id):

    referer = request.META.get('HTTP_REFERER', 'index')
    match = False

    for game in request.session.get('games_salvos'):
        if game.get('id') == id:
            match = True
    
    if not match:
        consumer = ConsumerAPI()
        game = consumer.detail_game(id)

        if request.session.get('games_salvos') == []:
            pass

        request.session['games_salvos'].append(game)
        request.session.save()

    return redirect(referer)

def deleteGame(request, id):

    referer = request.META.get('HTTP_REFERER', 'index')
    index = 0
    for game in request.session.get('games_salvos'):
        if game.get('id') == id:
            request.session.get('games_salvos').pop(index)
        else:
            index += 1
    request.session.save()
    return redirect(referer)

def savedGames(request):
    # pprint(request.session.get('games_salvos'))
    return render(request, 'games_salvos.html')

