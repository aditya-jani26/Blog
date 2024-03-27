from django.db import models
from django.utils.timezone import now


class members(models.Model):
    membersId = models.AutoField(primary_key=True, unique=True)
    uName = models.CharField(max_length=100, null=True, blank=True)
    uEmail = models.EmailField(max_length=100,null=True,unique=True)
    uPass = models.CharField(max_length=100,null=True,unique=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    images = models.ImageField(upload_to='profile')
    forgetPassToken = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)


class blog(models.Model):
    membersId = models.ForeignKey(members,on_delete=models.CASCADE,null=True)
    blogId = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    images = models.ImageField(upload_to='images/') 
    
class Comment(models.Model):
    membersId = models.ForeignKey(members, on_delete=models.CASCADE, null=True)
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE, null=True)
    comment_id = models.AutoField(primary_key=True)
    commentContent = models.TextField(max_length=300,null=True, blank=True)
    commentDate = models.DateTimeField(default=now)


class Follow(models.Model):
    follower = models.ForeignKey(members, related_name='following_relationships', on_delete=models.CASCADE)
    following = models.ForeignKey(members, related_name='followers_relationships', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class rating(models.Model):
    user = models.ForeignKey(members, on_delete=models.CASCADE)
    blogId = models.ForeignKey(blog, on_delete=models.CASCADE)
    ratingvalue = models.IntegerField(default=0)
    
class UserProfile(models.Model):
    user = models.OneToOneField(members, on_delete=models.CASCADE)
    following = models.ManyToManyField(members, related_name='followers', symmetrical=False)
# =================================================================

