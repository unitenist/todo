from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('create', views.create,name='create'),
    path('delete/<Todo_id>', views.delete,name='delete'),
    path('yesfinished/<Todo_id>', views.delete,name='yesfinished'),
    path('nofinished/<Todo_id>', views.delete,name='nofinished'),
]
