from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import *



urlpatterns = [
    path("", views.main,name="main"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login,name="login"),
    path("homepage/", views.homepage, name= "homepage"),
    path("addblog/", views.addblog, name="addblog"),
    path("myblog/", views.myblog,name="myblog"),
    path("add_comment/", views.add_comment, name="add_comment"),
    path("rating/", views.rating, name="rating"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_completed/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('changepass', views.changepass, name='changepass'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    # path("author_profiles/", views.author_profiles, name="author_profiles"),
