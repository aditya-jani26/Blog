
from django.contrib import admin
from.models import *

# class PersonModelAdmin(admin.ModelAdmin):
    # list_display = ["id", "name", "email"]
admin.site.register(blog)
class membersModelAdmin(admin.ModelAdmin):
    list_display = ["membersId", "uName", "uEmail"]
admin.site.register(members,membersModelAdmin)
admin.site.register(comments)
admin.site.register(rating)

# Register your models here.
