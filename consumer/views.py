from django.shortcuts import render
from django.http import HttpResponse
from utils.consumer import ConsumerAPI
from django.shortcuts import redirect

# Create your views here.
def index(request):
    consumer = ConsumerAPI()
    games = consumer.consume()
    return render(request, 'index.html', context={'games': games})

def filter(request, filter):
    print(filter)
    consumer = ConsumerAPI()
    games = consumer.consume()
    return render(request, 'index.html', context={'games': games})
    # plataforma = request.POST.get('plataforma')
    # categoria = request.POST.get('categoria')
    # ordem = request.POST.get('ordem')

    # filters = {
    #     'platform': plataforma, 
    #     'category': categoria,
    #     'sort': ordem
    # }

    # consumer = ConsumerAPI()
    # games = consumer.consume(filter=filters)

    # return render(request, 'index.html', context={'games': games})
    pass
    


