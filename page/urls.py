from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.main,name="main"),

    path("registration/", views.registration, name="registration"),
    path("login/", views.login,name="login"),
    path("home/", views.home, name="home"),
    path("addblog/", views.addblog, name="addblog"),
    path("profile/", views.profile, name="profile"),
    path("myblog/", views.myblog,name="myblog"),
    path("logout/", views.logout, name="logout"),
    path("add_comment/", views.add_comment, name="add_comment"),
    path("members_profile", views.members_profile, name="members_profile"),
    path("rating/", views.rating, name="rating"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path("change_password/", views.change_password, name="change_password"),

    # path("author_profiles/", views.author_profiles, name="author_profiles"),
