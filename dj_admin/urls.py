
from operator import index
from django.contrib import admin
from django.urls import path

from predire import views
from predire.views import resultat
app_name ='predire'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('resultat/', views.resultat, name='resultat'),
]
