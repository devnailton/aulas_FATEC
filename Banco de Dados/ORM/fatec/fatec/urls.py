from django.contrib import admin
from django.urls import path, include

from .views import HomeView #home_view

urlpatterns = [
    #path('', home_view, name='home'),   para view baseada em função
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('alunos.urls')),
]
