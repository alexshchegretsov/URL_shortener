from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from shortener.functions.base_62_encryption import base_62_encode
from shortener.functions.base_62_encryption import base_62_decode
from shortener.models import Url
from shortener.forms import UrlForm

HOST = 'http://127.0.0.1:8000'


def redirect_to_long_url(request, link_id):
    pass