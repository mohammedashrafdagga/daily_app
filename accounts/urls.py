from django.urls import path
from . import views as vs

app_name = 'accounts'
urlpatterns = [path('', vs.account_page, name='account-page')]
