from django.urls import path
from . import views as vs

app_name = 'main'
urlpatterns = [



    path('', vs.index, name='index'),
    path('create/', vs.create_note, name='create'),
    path('note_page/<str:serial_id>/', vs.note_page, name='note-page'),

]
