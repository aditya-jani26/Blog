from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class members(models.Model):
    membersId = models.AutoField(primary_key=True, unique=True)
    uName = models.CharField(max_length=100, null=True, blank=True)
    uEmail = models.EmailField(max_length=100,null=True,unique=True)
    uPass = models.CharField(max_length=100,null=True,unique=True)
    

    

class blog(models.Model):
    membersId = models.ForeignKey(members,on_delete=models.CASCADE,null=True)
    blogId = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')


    

class Comment(models.Model):
    membersId = models.ForeignKey(members, on_delete=models.CASCADE, null=True)
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE, null=True)
    comment_id = models.AutoField(primary_key=True)
    commentersName = models.CharField(max_length=100)
    commentContent = models.TextField(max_length=300)
    commentDate = models.DateTimeField(default=now)


    
class rating (models.Model):
    user = models.ForeignKey(members, on_delete=models.CASCADE)
    blogId = models.ForeignKey(blog, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)






# Create your models here.
# =================================================================
    # class blog
    # id,date,title,description,image
    #================================================================ 
    # class user 2
    # Id,UserName,UserEmail,UserPassword,status,number of posts created 
    # =================================================================

    # ----------------------------------------------------------------
    # class Admin3
    # Id,userName,useremail, number of posts,rattings given by user , remove user , add user
    # =================================================================

