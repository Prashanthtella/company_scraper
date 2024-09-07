# Create your views here.
from django.shortcuts import render
from .forms import KeywordForm
from .utils import scrape_data

def search_company(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            data = scrape_data(keyword)
            return render(request, 'scraper/results.html', {'data': data})
    else:
        form = KeywordForm()

    return render(request, 'scraper/search.html', {'form': form})
