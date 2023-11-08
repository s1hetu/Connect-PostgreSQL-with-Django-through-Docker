from django.urls import path

from .views import MigrationSuccessful

urlpatterns = [
    path('', MigrationSuccessful.as_view(), name='home'),
]
