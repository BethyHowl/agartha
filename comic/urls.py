from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'comic-home'),
    path('search/', views.search, name = 'comic-search'),
    path('description/', views.description, name = 'comic-description'),
    path('classifier/', views.classifier, name = 'comic-classifier'),
    path('stats/', views.stats, name = 'comic-stats'),
    path('recommender/', views.recommender, name = 'comic-recommender'),
]
