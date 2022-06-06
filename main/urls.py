from django.urls import path
from . import views as vs

app_name = 'main'
urlpatterns = [



    path('', vs.index, name='index')

]
