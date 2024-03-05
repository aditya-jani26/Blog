from django.shortcuts import render,redirect,get_object_or_404
import datetime
from .models import members
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.models import User
from .form import uform
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from .models import members, blog

# Create your views here.
# ====-home-=========================-home-=======================-home-============================================================
# this will show you link

def main(request):
    return render(request,'main.html')


# ====-register-=========================-register-=======================-register-================================================
# This is for new user 

def registration(request):
        if request.method == 'POST':

            uName = request.POST.get('uName')
            uEmail = request.POST.get('uEmail')
            uPass = request.POST.get('uPass')
            Enc_passworrd = make_password(uPass)

            newPerson = members(uName=uName, uEmail=uEmail, uPass=Enc_passworrd)
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
                Enc_passworrd = make_password(uPass)

            # user = request.user

                user = user = User.objects.get(username = "admin")
            # print(user)

                if members.objects.filter(uEmail=uEmail, uPass=uPass).exists():  
                    request.session['uEmail'] = uEmail
                    return redirect('home')
                elif members.objects.filter(uEmail=members.uEmail).exists() and check_password(uPass, members.uPass):
                    request.session['uEmail'] = uEmail
                    return redirect('home')
                else:
                    msg = 'Errors:Email  or password not is invalid' 
                    return render(request,"login.html",{"msg":msg})
        return render(request, 'login.html')
# ====-site-=========================-site-=======================-site-================================================
# This is the main main site where the user will reached after login
@login_required
def home(request):
    uEmail = request.session.get('uEmail')
    if uEmail:
        user_instance = get_object_or_404(members, uEmail=uEmail)
        myblog = members.objects.filter(membersId=user_instance.membersId) 
        return render(request,'home.html',{'myblog':myblog})    
    else:
        return redirect('login')
# ===========addblog======================addblog====================================addblog============================
    # This is used when any member want to add a new blog

def addblog(request): 

    if request.method == 'POST':
                date = datetime.date.today()
                title = request.POST.get('title')
                description = request.POST.get('description')
                
                obj= members.objects.get(uEmail=request.session['uEmail'])
                logedinUser = get_object_or_404(members,membersId=obj.membersId)
                # print(logedinUser.membersId)
                blogs = blog.objects.create(id=logedinUser.membersId, date=date, title=title, description=description)
                blogs.save()
                return redirect('home')
    return render(request,'addblog.html')


# def addblog(request): 
#     user_email = request.session.get('uEmail')
#     if user_email:
#         if request.method == 'POST':    
#             date = datetime.datetime.now()
#             title = request.POST.get('title')
#             description = request.POST.get('description')
#             image = request.FILES.get('image')
#             print('blog Image ',image)

#             obj = members.objects.get(uEmail=request.session['uEmail'])
#             user_instance = get_object_or_404(members, membersId=obj.membersId)

#             obj = blog.objects.create(id=user_instance, date=date, title=title, description=description, image=image)
#             fs = FileSystemStorage()
#             filename = fs.save(image.name, image)
#             uploaded_img_url = fs.url(filename)
#             obj.image = uploaded_img_url
#             obj.save()

#             return redirect('home')
#         return render(request,'addblog.html')
#     else:
#         return redirect('login')
            
# ====-myblog-=========================-myblog-=======================-myblog-=============
# In this all user will only see his own blog

def myblog(request):
     if request.method == 'GET':
    
        obj= members.objects.get(uEmail=request.session['uEmail'])
        logedinUser = get_object_or_404(members,membersId=obj.membersId)

        myblog = blog.objects.filter(id=logedinUser.membersId)
        return render(request, 'myblog.html', {'myblog': myblog})
     else:
        return redirect('login')
     
# ====-Home-=========================-Home-=======================-Home-=============
# this is will show all the blog posts

def home(request):

        myblog = blog.objects.all()
        return render(request, 'home.html', {'myblog': myblog})


# ====-logout-=========================-logout-=======================-logout-=============
# this will log out the user and delete the session
def logout(request):
    del request.session['uEmail']
    return render(request, 'login.html')


# =================================================================================================
# This is use to get profile of user and this will creatre profile page where the information of user will be available
def profile(request):
    context ={}
    context['form'] = uform
    return render(request, 'profile.html', context)
