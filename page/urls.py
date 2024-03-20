from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import *
from django.http import HttpResponse

def notification(request):
    return HttpResponse('THIS IS NOT A PAGE THIS JUST FOR TESTING PERFORMANCE TESTS')

urlpatterns = [
    path("", views.main,name="main"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login,name="login"),
    path("homepage/", views.homepage, name= "homepage"),
    path("addblog/", views.addblog, name="addblog"),
    path("myblog/", views.myblog,name="myblog"),
    path("admindash", views.admindash,name="admindash"),
    path("add_comment/<int:pk>/", views.add_comment, name="add_comment"),
    path("ratings/<int:pk>/", views.ratings, name="ratings"),

    path("profile/", views.profile, name="profile"),

    path("profile_details/<int:membersId>/",views.profile_details, name="profile_details"),

    path("handeuser/", views.handeuser, name="handeuser"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset_password_completed/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('changepass', views.changepass, name='changepass'),

    path('follow/<int:membersId>/', views.following, name='following'),
    path('unfollow/<int:membersId>/', views.unfollow, name='unfollow'),

    path("userDeactivate",views.userDeactivate, name='userDeactivate'),
    path("userActivate",views.userActivate, name='userActivate'),

    path("author_profiles/", views.author_profiles, name="author_profiles"),
    path("logout/", views.logout, name="logout"),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




