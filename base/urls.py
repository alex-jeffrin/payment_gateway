
from django.urls import path
from .views import home, success

urlpatterns = [
    path('donate/', home, name='home'),
    path('donate/success' , success , name='success')
]
