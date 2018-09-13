from django.urls import path
from example.views import user_list

app_name='example'
urlpatterns = [
    path('', user_list, name='user_list'),
]
