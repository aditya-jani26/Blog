
from django.contrib import admin
from.models import *

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
admin.site.register(blog)

class membersModelAdmin(admin.ModelAdmin):
    list_display = ["membersId", "uName", "uEmail","uPass"]
admin.site.register(members,membersModelAdmin)

class CommentAdmin(admin.ModelAdmin):   
    list_display = ["blog_id", "comment_id","commentersName","commentDate"]
admin.site.register(Comment)

class followModalAdmin(admin.ModelAdmin):
    list_display = ["follower", "followModalAdmin"]    
admin.site.register(Follow)

class ratingModelAdmin(admin.ModelAdmin):
    list_display = ["ratingvalue"]
admin.site.register(rating, ratingModelAdmin)

class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user"]
admin.site.register(UserProfile, UserProfileModelAdmin)

# Register your models here.
