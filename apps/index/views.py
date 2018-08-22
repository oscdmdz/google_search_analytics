from django.shortcuts import render
from google import google

from apps.index.forms.query import QueryForm


def index(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            search_results = google.search(request.POST['query'] + " " + request.POST['city'], 5)

            # <process form cleaned data>
            # return HttpResponseRedirect('/success/')
            return render(request, 'dashboard.html', {'form': form, 'search_results': search_results})
    else:
        form = QueryForm()

    return render(request, 'dashboard.html', {'form': form})
