import datetime
from django.contrib.auth.decorators import login_required
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
        print("User",user)
        if members.objects.filter(uEmail=uEmail).exists() and check_password(uPass, loginUser.uPass):  
            request.session['email'] = uEmail
            return redirect('homepage')
        elif User.objects.filter(email=user.email).exists() and check_password(uPass, request.user.password):
            request.session['email'] = user.email
            return redirect('adminDash')
        else:
            message = "Either Your Email Address or Password is incorrect...!!!"
            return render(request, "login.html", {'message':message})               
    return render(request, 'login.html')

# ===========addblog======================addblog====================================addblog============================
    # This is used when any member want to add a new blog
def addblog(request): 
    user_email = request.session.get('email')
    if user_email:
        if request.method == 'POST':
            date = datetime.date.today()
            time = datetime.datetime.now()
            title = request.POST.get('title')
            description = request.POST.get('description')
            images = request.FILES.get('images')
            obj= members.objects.get(uEmail=user_email)
            logedinUser = get_object_or_404(members,membersId=obj.membersId)
            # print(logedinUser.membersId)
            obj = blog.objects.create(membersId=logedinUser, date=date, title=title, description=description,images=images,time=time)
            fs = FileSystemStorage()

            filename = fs.save(images.name, images)
            uploaded_img_url = fs.url(filename)
            obj.images = uploaded_img_url
            obj.save()

            return redirect('addblog')
        return render(request,'addblog.html')
    else:
        return redirect('login')

# ====-myblog-=========================-myblog-=======================-myblog-=============
# # In this all user will only see his own blog
def myblog(request):
    user_email = request.session.get('email')
    if user_email:
        users = members.objects.get(uEmail=request.session['email'])
        user_instance = get_object_or_404(members, membersId = users.membersId)

        myblogs = blog.objects.filter(membersId=user_instance)
        loggedUser = members.objects.all()
        return render(request,'myblog.html',{'myblogs':myblogs, 'loggedUser':loggedUser})
    else:
        return redirect('login')

#====-site-=========================-site-=======================-site-================================================
# this is will show all the blog posts
    
@login_required
def homepage(request):
    user_email = request.session.get('email')
    if user_email:
        users = members.objects.all()
        logged_in_user = members.objects.get(uEmail=user_email)       
        blogs = blog.objects.all()
        blogs = blog.objects.exclude(membersId=logged_in_user)
        comments = Comment.objects.all()
        ratings = rating.objects.all()
        return render(request, 'homepage.html', {'blogs':blogs, 'comments':comments,'ratings':ratings,'users':users})
    else:
        return redirect('login')

# =========add_comment======================================add_comment=====================================add_comment=============

def add_comment(request, pk):
    user_email = request.session.get('email')
    if user_email:
        if request.method == 'POST':
            comment_content = request.POST.get('commentContent')
            user_instance = get_object_or_404(members, uEmail=user_email)
            blog_instance = get_object_or_404(blog, blogId=pk)
            
            new_comment = Comment.objects.create(
                blog_id=blog_instance,
                membersId=user_instance,
                commentContent=comment_content
            )
            new_comment.save()
            return redirect('homepage')
        else:
            blog_instance = get_object_or_404(blog, blogId=pk)
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
            
            ratingValue = request.POST.get('ratingValue')

            obj = members.objects.get(uEmail=request.session['email'])
            user_instance =  get_object_or_404(user_email,membersId=obj.membersId)
            blog_instance = get_object_or_404(blog, blogId=pk)  
            if user_instance.uEmail != blog_instance.membersId.uEmail:
              rating.objects.update_or_create(blogId=blog_instance, membersId=user_instance,defaults={'ratingValue': ratingValue})

            return redirect('homepage')
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

        users = members.objects.filter(uEmail=user_email)
        # This is used to see the crrent user is varified user or not (logedin with password)
        user = get_object_or_404(members, uEmail=user_email)
        #This is used to check if the user is another user is in members table list (is present in the user table)
        user_profile = get_object_or_404(UserProfile, user=user)
        # this will create the profile if not present in the user table
        followers_count = UserProfile.objects.count()
        # this will use inbuild function which is .counter method
        Logged_user_following = UserProfile.objects.filter(another_user__another_user__user_id=user)
        # user_followings = UserProfile.objects.filter(blogId__membersId=user)
        #this user_followings will be user .filter to filter followers from member table
        followings = Logged_user_following.count()
        # This followings is useing .count method ro count total number of following 
        # this print is used to check if the followings has any value in it or not.
        return render(request, 'profile_detail.html', {'user': users, 'user_profile':user_profile, 'loggedUser':Logged_user_following , 'followers_count':followers_count,'followings':followings })
    else:
        return redirect('login')
# =================================================================profile_details ====================================================
    # this fuction is user to see whoes blog post is it and 
def profile_details(request):
    user_email = request.session.get("email")
    if user_email:
        # if the email is in session then this will move forward
        user = members.objects.filter(uEmail=user_email)
        # this wil store " .filter output " from member table of the session this user has (loged in user)
        user_instance = members.objects.get(uEmail=user_email)
        # this will " .get the value from members table " and store it in user_instance
        user_profile = get_object_or_404(UserProfile, user=user)
        # this will see if user from member table and this user is in this model table ot not -> if not it will show that in model this is not present
        followers_count = user_profile.followers.count()
        # followers_count this will use " .count " method and count user profile and store it in followers_count 
        Logged_user_followings = UserProfile.objects.filter(followers=user)
        # with the help of " .filter " method it will go in this UserProfile table and try to get value of session user Logged_user_followings
        followings = Logged_user_followings.count()
        # then simply this will use" .count method "and store total number of Logged_user_followings 
        return render(request, 'profile.html', {'users': user_instance, 'followers_count':followers_count,'followings':followings })
    else:
        return redirect('login')
# =================================================================following =================================================================
def following(request, membersId):
    user_email = request.session.get('email')
    if request.method == 'POST' and user_email:
        user_to_follow = get_object_or_404(members, membersId=membersId)
        # this variable is used to keep track of user is  folowed or not if not then it will create and save it in this variable
        following_user = get_object_or_404(members, uEmail=user_email)
        # this variable  is user to check if the following_user is a following the user(logedin user or not )
        user_profile = UserProfile.objects.get_or_create(user=user_to_follow)
        # this use get or create method in this case if the user is folowing the outher account then it will get or it will create a new account
        user_profile.followers.add(following_user)
        # after creating or getting the user the above value of user_profile will add with .add method in case number 2 that id following_user.
        return redirect('profile_details', membersId=membersId)
    else:
        return redirect('login')

# # =================================================================unfollow =================================================================
    
def unfollow(request, membersId):
    user_email = request.session.get('email')
    if request.method == 'POST' and user_email:
        user_to_unfollow = get_object_or_404(members, membersId=membersId)

        following_user = get_object_or_404(members, userEmail=user_email)

        user_profile= UserProfile.objects.get_or_create(user=user_to_unfollow)
        # this varibale will user_profile get or create the vaue if the user is in user_to_unfollow, if not then it will create and store it in this user_to_unfollow
        user_profile.followers.remove(following_user)
        #  user_profile is useing .remove method to remove and the store it in following_user which will show the user.
        return redirect('profile_detail', membersId=membersId)
    else:
        return redirect('login')

# =================================================================================================
# ============================activate=====================================
# activate and deactivate members
@login_required
def userDeactivate(request, id):
    user = get_object_or_404(members, user_id=id)
    user.is_active = False
    # this is useing .is_active method see if that value is False ()
    user.save()
    return redirect(handeuser)

# =================================================================
@login_required
def userActivate(request, id):
    user = get_object_or_404(members, user_id=id)
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
@login_required
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