from django.urls import path
from .views.form_handler import url_form_handler
from .views.redirect_to import redirect_to_long_url

urlpatterns = [
    path('', url_form_handler),
    path('<str:link_id>/', redirect_to_long_url),
]
