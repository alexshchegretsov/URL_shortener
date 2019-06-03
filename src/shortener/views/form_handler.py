from django.shortcuts import render
from django.http import HttpResponse

from shortener.functions import base_62_encode
from shortener.models import Url
from shortener.forms import UrlForm

HOST = 'http://127.0.0.1:8000'


def url_form_handler(request):
    urls_from_db = Url.objects.all()[:5]
    if request.method == 'GET':
        context = {'form': UrlForm(), 'urls_from_db': urls_from_db, 'HOST': HOST}
        return render(request, 'shortener/home_page.html', context)
    elif request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data.get('long_url')

            if Url.objects.filter(long_url=long_url).exists():
                current_url = Url.objects.get(long_url=long_url)
                context = {'short_url': f'{HOST}/{current_url.short_url}', 'HOST': HOST}
                return render(request, 'shortener/to_short_url.html', context)
            else:
                current_url = Url(long_url=long_url)
                current_url.save()
                current_url.short_url = base_62_encode(current_url.id)
                current_url.save()
                context = {'short_url': f'{HOST}/{current_url.short_url}', 'HOST': HOST}
                return render(request, 'shortener/to_short_url.html', context)
        else:
            errors = form.errors
            return HttpResponse(errors)
    else:
        return HttpResponse('INVALID REQUEST')
