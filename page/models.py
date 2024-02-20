from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class members(models.Model):
    membersId = models.IntegerField(primary_key=True)
    uName = models.CharField(max_length=100)
    uEmail = models.EmailField(max_length=100,unique=True)
    uPass = models.CharField(max_length=100)
    

    def __str__(self):
        return self.uName

class comments(models.Model):
    person = models.ForeignKey(members,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.person.uName
    
class rating (models.Model):
    user = models.ForeignKey(members, on_delete=models.CASCADE)
    postid = models.ForeignKey(blog, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.title}: {self.rating}"





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

