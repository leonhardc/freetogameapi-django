from django.shortcuts import render
from django.http import HttpResponse
from utils.consumer import ConsumerAPI
from django.shortcuts import redirect

# Create your views here.
def index(request):
    plataforma = request.GET.get('plataforma')
    categoria = request.GET.get('categoria')
    ordem = request.GET.get('ordem')
    url = 'https://www.freetogame.com/api/games?'
    
    if plataforma=='' and categoria=='' and ordem=='':
        consumer = ConsumerAPI()
        games = consumer.consume()
        return render(request, 'index.html', context={'games': games})

    if plataforma:
        url += f'platform={plataforma}'
        if categoria:
            url += f'&category={categoria}'
        if ordem:
            url += f'&sort={ordem}'

        consumer = ConsumerAPI()
        games = consumer.consume(url=url)
        return render(request, 'index.html', context={'games': games})
    
    elif categoria:
        url += f'category={categoria}'
        if ordem:
            url += f'&sort={ordem}'

        consumer = ConsumerAPI()
        games = consumer.consume(url=url)
        return render(request, 'index.html', context={'games': games})

    elif ordem:
        url += f'sort={ordem}'

        consumer = ConsumerAPI()
        games = consumer.consume(url=url)
        return render(request, 'index.html', context={'games': games})
    
    consumer = ConsumerAPI()
    games = consumer.consume()
    return render(request, 'index.html', context={'games': games})


