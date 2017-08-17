from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from django.template import RequestContext



from .models import Game, Environment

def index(request):
    latest_games_list = Game.objects.order_by('-pub_date')[:5]
    context = {'latest_games_list': latest_games_list}
    return render(request, 'liefspelen/index.html', context)

def detail(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Spel is niet gevonden")
    return render(request, 'liefspelen/detail.html', {'game': game})  

def recipe(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Recept is niet gevonden")
    return render(request, 'liefspelen/detail_recipe.html', {'game': game})  

def worksheet(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Werkblad is niet gevonden")
    return render(request, 'liefspelen/detail_worksheet.html', {'game': game})  


def buiten(request):
    return render(request, 'liefspelen/buiten.html', {})

def binnen(request):
    return render(request, 'liefspelen/binnen.html', {})

def tuin(request):
    latest_games_list = Game.objects.filter(environments__env_name='Tuin')
    location = "In de tuin"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def bos(request):
    latest_games_list = Game.objects.filter(environments__env_name='Bos')
    location = "In het bos"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def strand(request):
    latest_games_list = Game.objects.filter(environments__env_name='Strand')
    location = "In het zand"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def schoolplein(request):
    latest_games_list = Game.objects.filter(environments__env_name='Schoolplein')
    location = "Op de tegels"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def zwembad(request):
    latest_games_list = Game.objects.filter(environments__env_name='Zwembad')
    location = "Plons!"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def koken(request):
    latest_games_list = Game.objects.filter(categories__cat_name='Koken')
    location = "Tussen potten en pannen"
    origin = request.path
    context = {'latest_games_list': latest_games_list, 'location': location, 'origin': origin}
    return render(request, 'liefspelen/list.html', context)

def spelletjes(request):
    latest_games_list = Game.objects.filter(categories__cat_name='Spelletjes')
    location = "Tussen pionnen en dobbelstenen"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def gym_ideetjes(request):
    latest_games_list = Game.objects.filter(categories__cat_name='Gym-ideetjes')
    location = "Tussen de lijnen"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)


def handwerken(request):
    latest_games_list = Game.objects.filter(categories__cat_name='Handwerken')
    location = "Tussen de draadjes en naalden"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def werkbladen(request):
    latest_games_list = Game.objects.filter(categories__cat_name='Werkbladen')
    location = "Tussen cijfers en letters"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

def knutselen(request):
    latest_games_list = Game.objects.filter(categories__cat_name='Knutselen')
    location = "Tussen papiersnippers en lijmresten"
    context = {'latest_games_list': latest_games_list, 'location': location}
    return render(request, 'liefspelen/list.html', context)

