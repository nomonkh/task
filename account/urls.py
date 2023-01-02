from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('signup/', registration_view, name='signup'),
    path('', authentication, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('update/', update_account, name='update_account'),

]
