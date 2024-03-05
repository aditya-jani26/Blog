from django.db import models
from django.contrib.auth.models import User


class members(models.Model):
    membersId = models.AutoField(primary_key=True, unique=True)
    uName = models.CharField(max_length=100)
    uEmail = models.EmailField(max_length=100,null=True,unique=True)
    uPass = models.CharField(max_length=100)
    

    def __str__(self):
        return self.uName
    

class blog(models.Model):
    membersId = models.ForeignKey(members,on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class comments(models.Model):
    person = models.ForeignKey(members,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.person.membersId
    
class rating (models.Model):
    user = models.ForeignKey(members, on_delete=models.CASCADE)
    postid = models.ForeignKey(blog, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.postid}: {self.rating}"





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

