from django.http import HttpResponse
from django.shortcuts import render

from stock.utils import varsha, get_local
from stock.utils import top
#from stock.utils import scraper

# Create your views here.


def index(request):
    #scraper.scr_call()
    return render(request, 'stock/index.html', context_instance=None)


def dashboard(request):
    return render(request, 'stock/dashboard.html', context_instance=None)


def reports(request):
    return render(request, 'stock/reports.html', context_instance=None)


def topg(request):
    gainers = top.top_gainers()
    losers = top.top_losers()
    con = {
        'gainers': gainers,
        'losers': losers,
    }
    return render(request, 'stock/topg.html', con, context_instance=None)


def current(request):
    return render(request, 'stock/current.html', context_instance=None)


def today(request):
    return render(request, 'stock/today.html', context_instance=None)


def experts(request):
    return render(request, 'stock/experts.html', context_instance=None)


def company_reviews(request):
    return render(request, 'stock/company_reviews.html', context_instance=None)


def todays_comments(request):
    return render(request, 'stock/todays_comments.html', context_instance=None)


def graph(request):
    return render(request, 'stock/graph.html', context_instance=None)


def try_python(request):
    result = varsha.x()
    return render(request, 'stock/trial.html', {'result':result})


