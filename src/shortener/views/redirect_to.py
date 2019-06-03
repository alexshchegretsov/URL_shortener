from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from shortener.functions import base_62_decode
from shortener.models import Url


def redirect_to_long_url(request, link_id):
    if request.method == 'GET':
        id = base_62_decode(link_id)
        url = get_object_or_404(Url, id=id)
        url.count += 1
        url.save()
        return redirect(url.long_url)
    return HttpResponse('INVALID REQUEST')
