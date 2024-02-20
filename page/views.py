from django.shortcuts import render,redirect,get_object_or_404
import datetime
from django.http import HttpResponse
from .models import members,comments,rating,blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.models import User

# Create your views here.
# ====-home-=========================-home-=======================-home-============================================================
# this will show you link

def main(request):
    return render(request,'home.html')


# ====-register-=========================-register-=======================-register-================================================
# This is for new user 

def registration(request):
        if request.method == 'POST':

            uName = request.POST.get('uName')
            uEmail = request.POST.get('uEmail')
            uPass = request.POST.get('uPass')

            newPerson = members(uName=uName, uEmail=uEmail, uPass=uPass)
            newPerson.save()

            request.session['uEmail'] = uEmail
            return redirect("login")
        return render(request,'registration.html')

# ====-login-=========================-login-=======================-login-================================================
# This is used for members of the the site

def login(request):
        if request.method == 'POST':
                uEmail = request.POST.get('uEmail')
                uPass = request.POST.get('uPass') 

            # user = request.user

                user = user = User.objects.get(username = "admin")
            # print(user)

                if members.objects.filter(uEmail=uEmail, uPass=uPass).exists():  
                    request.session['email'] = uEmail
                    return redirect('site')
                elif members.objects.filter(email=user.email).exists() and check_password(uPass, members.uPass):
                    request.session['email'] = uEmail
                    return redirect('site')
                else:
                    return HttpResponse("Either email or password is incorrect.")
        return render(request, 'login.html')
# ====-site-=========================-site-=======================-site-================================================
# This is the main main site where the user will reached after login
@login_required
def site(request):
    uEmail = request.session.get('email')
    if uEmail:
        user_instance = get_object_or_404(members, uEmail=uEmail)
        myblog = members.objects.filter(membersId=user_instance.membersId) 
        return render(request,'site.html',{'myblog':myblog})    
    else:
        return redirect('login')
# ===========addblog======================addblog====================================addblog============================
    # This is used when any member want to add a new blog
@login_required
def addblog(request):
            
        if request.method == 'POST':
            date = datetime.date.today()
            title = request.POST.get('title')
            description = request.POST.get('description')
            
            obj= members.objects.get(email=request.session['email'])
            logedinUser = get_object_or_404(members,id=obj.id)
            new_todo = blog.objects.create(user_id=logedinUser, date=date, title=title, description=description)
            new_todo.save()
   
            return redirect('site')
        return render(request,'site.html')
        
# ====-myblog-=========================-myblog-=======================-myblog-=============
# In this all user will only see his own blog

@login_required
def myblog(request):
     if request.method == 'GET':
        uEmail = request.session.get('email')
    
        obj= members.objects.get(email=request.session['email'])
        logedinUser = get_object_or_404(members,id=obj.id)
        return render(request, 'site.html', {'myblog': myblog})
     else:
        return redirect('login')
     
# ====-Home-=========================-Home-=======================-Home-=============
# this is will show all the blog posts
@login_required
def home(request):
    uEmail = request.session.get('email')
    if uEmail in members:
        myblog = blog.objects.all()
    else:
        return redirect('login')
    
    return render(request, 'site.html', {'Home': home})


# ====-logout-=========================-logout-=======================-logout-=============
# this will log out the user and delete the session
def logout(request):
    del request.session['email']
    return render(request, 'login.html')


# =================================================================================================