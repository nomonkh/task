from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

from personal.views import (
    home_sreen_view,
)
from upload.account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)

urlpatterns = [
    path('', home_sreen_view, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('blog/', include('blog.urls', 'blog')),
    path('login/', login_view, name='login'),
    path('must_authenticate/', must_authenticate_view, name='must_authenticate'),
    path('account/', account_view, name='account'),
    path('admin/', admin.site.urls),

    # REST FRAMEWORK URLS
    path('api/blog/', include('blog.api.urls', 'blog_api')),
    path('api/account/', include('upload.account.api.urls', 'account_api')),


    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)