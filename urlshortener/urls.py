from django.urls import path

from urlshortener import views

urlpatterns = [
    path('<uuid:shortcut>', views.redirect_to_address),
    path('', views.get_url)
]
