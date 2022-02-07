from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('boards/<int:id>/', views.boards_topic, name='boards_topic')

]
