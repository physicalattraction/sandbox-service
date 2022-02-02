from django.urls import path

from sleep.views import async_sleep, sync_sleep

urlpatterns = [
    path('api/sync_sleep/', sync_sleep, name='sync_sleep'),
    path('api/async_sleep/', async_sleep, name='async_sleep'),
]
