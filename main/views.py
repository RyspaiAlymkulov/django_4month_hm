from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from main.models import Film, Review


# Create your views here.


def index_html(request):
    return render(request, 'index.html')


def index(request):
    current_time = datetime.now().strftime('%H:%M:%S')
    html = "<html><body><b>Current Time Value:</b> %s</body></html>" % current_time
    return HttpResponse(html)


def film_views(request):
    lists = Film.objects.all()
    context = {
        'film_list': lists
    }
    return render(request, 'film.html', context=context)


def film_item_view(request, id):
    details = Film.objects.get(id=id)
    contexts = {
        'film_detail': details,
        'reviews': Review.objects.filter(film_id=id)
    }
    return render(request, 'detail.html', context=contexts)


def category_films(request, id):
    context = {
        'film_list': Film.objects.filter(category_id=id)
    }
    return render(request, 'film.html', context=context)