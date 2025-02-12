from django.urls import path
from . import views

urlpatterns = [
    path('<str:month>', views.monthly_challenge),
    path('<int:month>', views.monthly_challenge_by_number)
]
