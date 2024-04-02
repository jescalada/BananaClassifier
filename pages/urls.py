from django.urls import path
from .views import homePageView, aboutPageView, juanPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('juan/', juanPageView, name='juan'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:size>/<int:weight>/<int:sweetness>/<int:softness>/<int:harvestTime>/<int:ripeness>/<int:acidity>', results, name='results'),
]
