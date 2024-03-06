from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.main,name="main"),

    path("registration/", views.registration, name="registration"),
    path("login/", views.login,name="login"),
    path("home/", views.home, name="home"),
    # path("blogs", views.blogs,name="blogs"),
    path("addblog/", views.addblog, name="addblog"),
    path("profile/", views.profile, name="profile"),
    path("myblog/", views.myblog,name="myblog"),
    path("logout/", views.logout, name="logout"),
    path("add_comment/", views.add_comment, name="add_comment"),
]
    # path("rating/", views.rating, name="rating"),
    # path("comments/", views.comments, name="comments"),

    # path("profile/", views.profile, name="profile"),
    # path("edit_profile/", views.edit_profile, name="edit_profile"),
    # path("delete_profile/", views.delete_profile, name="delete"),
    # path("change_password/", views.change_password, name="change_password"),

    # path("author_profiles/", views.author_profiles, name="author_profiles"),
