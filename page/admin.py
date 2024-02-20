
from django.contrib import admin
from.models import *

# class PersonModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "email"]
admin.site.register(blog)
admin.site.register(members)
admin.site.register(comments)
admin.site.register(rating)

# Register your models here.
