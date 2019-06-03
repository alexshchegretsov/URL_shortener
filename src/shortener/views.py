from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .functions.base_62_encryption import base_62_encode
from .functions.base_62_encryption import base_62_decode
from .models import Url
from .forms import UrlForm

HOST = 'http://127.0.0.1:8000'


def url_form_handler(request):
    pass


def redirect_to_real_url(request, link_id):
    pass

