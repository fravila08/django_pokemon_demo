from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    #here I am telling this url path '' to use the home view to render any and all information.
]
