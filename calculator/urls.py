
from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:num_1>/<int:num_2>/', add),
    path('sub/<int:num_1>/<int:num_2>/', sub),
    path('mult/<int:num_1>/<int:num_2>/', mult),
    path('div/<int:num_1>/<int:num_2>/', div),
]
