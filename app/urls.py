from django.urls import path, re_path
from app import views



urlpatterns = [
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    path('show', views.show, name='show'),
    path('maps', views.maps, name='maps'),
]
