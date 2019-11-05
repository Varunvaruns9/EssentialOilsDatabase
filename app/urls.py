from django.urls import path

from . import views


urlpatterns = [
    # Url for main query page.
    path('', views.index, name='index'),
    # Url for csv upload form.
    path('load/', views.load, name='load'),
    # Url for user manual.
    path('manual/', views.manual, name='manual'),
]
