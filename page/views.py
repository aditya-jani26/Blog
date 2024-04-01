import datetime
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# from django.urls import reverse_lazy
# from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
# from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
# ====-link-=========================-link-=======================-link-============================================================
# this will show you link
def main(request):
    return render(request,'main.html')
# ====-adminDash-========================
def admindash(request):
    user_email = request.session.get('email')
    if user_email:
        blogs = blog.objects.all()
        comments = Comment.objects.all()
        return render(request, 'adminDash.html',{'blogs':blogs, 'comments':comments})
    else:
        return redirect('login')
# ====-register-=========================-register-=======================-register-================================================
# This is for new user
def registration(request):
        if request.method == 'POST':

            uName = request.POST.get('uName')
            uEmail = request.POST.get('uEmail')
            uPass = request.POST.get('uPass')
            about = request.POST.get('about')
            images = request.FILES.get('images')
            # name="images"
            Enc_passworrd = make_password(uPass)
            newPerson = members.objects.create(uName=uName, uEmail=uEmail, uPass=Enc_passworrd,images=images,about=about)
            fs = FileSystemStorage()
            filename = fs.save(images.name, images)
            uploaded_img_url = fs.url(filename)
            newPerson.images = uploaded_img_url
            newPerson.save()
            return redirect("login")
        return render(request,'registration.html')
# ====-login-=========================-login-=======================-login-================================================
# This is used for members of the the site
def login(request):

    if request.method == 'POST':    
        uEmail = request.POST.get('uEmail')
        uPass = request.POST.get('uPass') 
        try:
            loginUser = members.objects.get(uEmail=uEmail)
        except Exception as e:
            loginUser = None
        user = request.user
        # print("User",user)
        if members.objects.filter(uEmail=uEmail).exists() and check_password(uPass, loginUser.uPass):  
            request.session['email'] = uEmail
            return redirect('homepage')
        elif User.objects.filter(email=user.email).exists() and check_password(uPass, request.user.password):
            request.session['email'] = user.email
            return redirect('admindash')
        else:
            message = "Either Your Email Address or Password is incorrect...!!!"
            return render(request, "login.html", {'message':message})               
    return render(request, 'login.html')

# ===========addblog======================addblog====================================addblog============================
def addblog(request):
    user_email = request.session.get('email')
    
    if user_email:
        if request.method == 'POST':
            # Fetching necessary data
            logged_in_user = get_object_or_404(members, uEmail=user_email)
            
            # Extracting form data
            title = request.POST.get('title')
            description = request.POST.get('description')
            images = request.FILES.get('images')
            
            # Saving blog entry
            new_blog_entry = blog.objects.create(
                membersId=logged_in_user,
                date=datetime.date.today(),
                title=title,
                description=description,
                images=images,
                time=datetime.datetime.now()
            )
            
            # Saving uploaded image
            fs = FileSystemStorage()
            filename = fs.save(images.name, images)
            uploaded_img_url = fs.url(filename)
            new_blog_entry.images = uploaded_img_url
            new_blog_entry.save()
            
            return redirect('addblog')
        
        return render(request, 'addblog.html')
    else:
        return redirect('login')
# ====-myblog-=========================-myblog-=======================-myblog-=============
# # In this all user will only see his own blog
def myblog(request):
    user_email = request.session.get('email')
    
    if user_email:
        # Fetching necessary data
        user_instance = get_object_or_404(members, uEmail=user_email)
        
        # Retrieving user's blogs
        myblogs = blog.objects.filter(membersId=user_instance)
        
        # Fetching all logged-in users
        logged_users = members.objects.all()
        
        return render(request, 'myblog.html', {'myblogs': myblogs, 'loggedUser': logged_users})
    else:
        return redirect('login')
#====-site-=========================-site-=======================-site-================================================
# this is will show all the blog posts
    

def homepage(request):
    user_email = request.session.get('email')
    if user_email:
        # Fetch logged in user
        logged_in_user = members.objects.filter(uEmail=user_email).first()
        
        if logged_in_user:
            # Fetch all users
            users = members.objects.all()

            # Fetch blogs excluding those of logged in user
            blogs = blog.objects.exclude(membersId=logged_in_user)
            
            # Fetch all comments
            comments = Comment.objects.all()
            
            # Fetch all ratings
            ratings = rating.objects.all()
            
            return render(request, 'homepage.html', {'blogs': blogs, 'comments': comments, 'ratings': ratings, 'users': users})
        
    return redirect('login')
# =========add_comment======================================add_comment=====================================add_comment=============

def add_comment(request, pk):
    user_email = request.session.get('email')
    if user_email:
        user_instance = get_object_or_404(members, uEmail=user_email)
        blog_instance = get_object_or_404(blog, blogId=pk)

        if request.method == 'POST':
            comment_content = request.POST.get('commentContent')
            new_comment = Comment.objects.create(
                blog_id=blog_instance,
                membersId=user_instance,
                commentContent=comment_content
            )
            return redirect('homepage')
        else:
            comments_list = Comment.objects.filter(blogId=blog_instance)
            return render(request, 'homepage.html', {'blog_instance': blog_instance, 'comments': comments_list})
    else:
        return redirect('login')
# -= ===============rating==================================rating=============rating================================ 
    # one errror (.update is not working yet; it is only creating new ratingalways)
def ratings(request, pk):
    user_email = request.session.get('email')
    if user_email:
        if request.method == 'POST':
            
            ratingvalue = request.POST.get('ratingvalue')
            print("rating value",ratingvalue)
            obj = members.objects.get(uEmail=request.session['email'])  
            print("user obj",obj)
            user_instance =  get_object_or_404(members,membersId=obj.membersId)
            print("user user_instance",user_instance)
            blog_instance = get_object_or_404(blog, blogId=pk)
            print("user blog_instance",blog_instance)
            print("pk",pk)

            if user_instance.uEmail != blog_instance.membersId.uEmail:
                rating.objects.update_or_create(blogId=blog_instance, user=user_instance, defaults={'ratingvalue': ratingvalue})
                return redirect('homepage')
            else:
                return redirect('login')
    else:
        return redirect('login') 
# ==========================================changePass======================changePass======================
    # done
    # This is use to change the password within the site page
def changepass(request):
    user_email = request.session.get('email')

    if user_email:

        if  request.method == 'POST':
            old_pass = request.POST.get('oldPass')
            new_pass = request.POST.get('newPass')
            confirm_pass = request.POST.get('confirmPass')
        
            user = members.objects.get(uEmail=request.session['email'])

            if user and check_password(old_pass, user.uPass):
                if new_pass == confirm_pass:
                    user.uPass = make_password(new_pass)
                    user.save()
                    return redirect('login')
                else:
                    message = "New Passwords do not match"
                    return render(request, "changePass.html", {'message':message})
            else:
                message = "Old Passwords do not match"
                return render(request, "changePass.html", {'message':message})
        users = members.objects.all()
        return render(request, 'changePass.html', {'users':users})
    else:
        return redirect('login')

# ====profile=========================================profile==============================================profile======
# This is use to get profile of user and this will creatre profile page where the information of user will be available
# this will show the profile of user who is logged in.

def profile(request):
    user_email = request.session.get('email')
    if user_email:
        user = get_object_or_404(members, uEmail=user_email)
        user_profile, _ = UserProfile.objects.get_or_create(user=user)
        followers_count = user_profile.following.count()
        logged_user_followings = followers_count  # No need for separate count() call
        avg_rating = rating.objects.filter(blogId__membersId=user).aggregate(avg_rating=models.Avg('ratingvalue'))
        avg = round(avg_rating['avg_rating'], 2) if avg_rating['avg_rating'] is not None else 0
        print("avg", avg)
        return render(request, 'profile.html', {'user': user, 'followers_count': followers_count, 'avg': avg, 'followings': logged_user_followings})
    else:
        return redirect('login')
    
def profile_detail(request, membersId):
    user_email = request.session.get("email")
    if user_email:
        user = get_object_or_404(members, membersId=membersId)
        logged_user = get_object_or_404(members, uEmail=user_email)
        user_profile, _ = UserProfile.objects.get_or_create(user=user)
        followers_count = user_profile.following.count()
        user_followings = UserProfile.objects.filter(following=user).count()
        avg_rating = rating.objects.filter(blogId__membersId=user).aggregate(avg_rating=models.Avg('ratingvalue'))
        avg = round(avg_rating['avg_rating'], 2) if avg_rating['avg_rating'] is not None else 0
        return render(request, 'profile_detail.html', {'user': user, 'user_profile': user_profile, 'logged_user': logged_user, 'followers_count': followers_count, 'user_followings': user_followings, 'avg_rating': avg})
    else:
        return redirect('login')
def follow(request, membersId):
    user_email = request.session.get('email')
    if request.method == 'POST' and user_email:
# Inside this condition, it retrieves the members object corresponding to the membersId provided in the URL:
        user_to_follow = get_object_or_404(members, membersId=membersId)
# It also retrieves the members object corresponding to the currently logged-in user using their email:
        following_user = get_object_or_404(members, uEmail=user_email)
# It then gets or creates a UserProfile object associated with the user to be followed:
        user_profile, _ = UserProfile.objects.get_or_create(user=user_to_follow)
# It adds the currently logged-in user (retrieved in step 5) to the list of users that the user represented by user_profile is following:
        user_profile.following.add(following_user)

        return redirect('profile_detail', membersId=membersId)
    else:
        return redirect('login')



def unfollow(request, membersId):
    user_email = request.session.get('email')
    if request.method == 'POST' and user_email:
        user_to_unfollow = get_object_or_404(members, membersId=membersId)
        following_user = get_object_or_404(members, uEmail=user_email)
        user_profile, _ = UserProfile.objects.get_or_create(user=user_to_unfollow)
        user_profile.following.remove(following_user)
        return redirect('profile_detail', membersId=membersId)
    else:
        return redirect('login')
# =================================================================================================
# ============================activate=====================================
# activate and deactivate members

def userDeactivate(request, id):
    user = get_object_or_404(members, membersId=id)
    user.is_active = False
    # this is useing .is_active method see if that value is False ()
    user.save()
    return redirect(handeuser)

# =================================================================

def userActivate(request, id):
    user = get_object_or_404(members, membersId=id)
    user.is_active = True
    # this is using .is_active method and see this value of user(member) value with this method is coming true or not.
    user.save()
    return redirect(handeuser)
# =================================================================
def admindash(request):
    user_email = request.session.get('email')
    if user_email:  
        blogs = blog.objects.all()
        comments = Comment.objects.all()
        return render(request, 'admindash.html',{'blogs':blogs, 'comments':comments})
    else:
        return redirect('login')
#==============================handeuser======================================== 

def handeuser(request):
    user_email = request.session.get('email')
    if user_email:
        authors = members.objects.all()
        return render(request, 'handeluser.html',{'authors': authors})
    else:
        return redirect('login')
# =================================================================
def author_profiles(request):
    user=request.session.get('email')
    if user:
        authors = members.objects.all()
        return render(request, 'author_profiles.html',{'authors': authors})
# ===============================-=-logout-=========================-logout-=======================-logout-=============
# this will log out the user and delete the session
def logout(request):
    del request.session['email']
    return render(request, 'login.html')
# =================================================================