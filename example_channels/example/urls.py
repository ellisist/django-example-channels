from django.urls import path
from example.views import log_in, log_out, sign_up, user_list

app_name='example'
urlpatterns = [
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('sign_up/', sign_up, name='sign_up'),
    path('', user_list, name='user_list'),
]
