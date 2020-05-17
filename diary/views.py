from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from diary.models import DiaryEntries, Owner, Feedback
from django.conf import settings 
from django.core.mail import send_mail
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        fullname=request.POST["fullname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        diaryname=request.POST["diaryname"].upper()
        first_name=fullname.split()[0]
        last_name=" ".join(fullname.split()[1:])
        user= User.objects.create_user(
            first_name=first_name,
            last_name=last_name, 
            username=username, 
            password=password, 
            email=email
        )
        login(request, user)
        subject = 'Welcome to "writemydiary" world.'
        message = f'Hi {user.username}, glad that you registered to writemydiary. You will have great experience using it. Make diary writing as your habit from today.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail( subject, message, email_from, recipient_list )
        ownerdiary=Owner.objects.create(
            user=user,
            diaryname=diaryname
        )
        return redirect("/dashboard/")
    return render(request,"signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in successfully")
            return redirect("/dashboard/")
        else:
            messages.info(request,"Invalid email or password")
        return redirect("/signup/")
    return render(request,"signin.html")

def signout(request):
	logout(request)
	return render(request,"logout.html")

# @login_required
def dashboard(request):
    user=request.user
    owner=Owner.objects.get(user=user)
    all_diaries=DiaryEntries.objects.filter(user=user).order_by('-timestamp')
    return render(request,"dashboard.html",{"all_diaries":all_diaries, "owner":owner})

# @login_required
def diary_specific(request,DiaryEntries_id):
    user=request.user
    owner=Owner.objects.get(user=user)
    viewdiary=DiaryEntries.objects.get(pk=DiaryEntries_id)
    return render(request,"diary_specific.html",{"viewdiary":viewdiary, "owner":owner})

# @login_required
def create_diary(request):
    user=request.user
    owner=Owner.objects.get(user=user)
    if request.method == "POST":
        highlight = request.POST["highlight"]
        diarycontent = request.POST.get("diarycontent")
        

        diary_instance = DiaryEntries(
                highlight=highlight,
                diarycontent=diarycontent,
                user = request.user,

        	)
        diary_instance.save()
        messages.success(request,"Diary created successfully")
        return redirect("/dashboard/")
    
    return render(request,"create_diary.html",{"owner":owner})

# @login_required
def edit_diary(request,DiaryEntries_id):
    user=request.user
    owner=Owner.objects.get(user=user)
    diary_instance=DiaryEntries.objects.get(pk=DiaryEntries_id)
    if request.method == "POST":
        highlight = request.POST["highlight"]
        diarycontent = request.POST["diarycontent"]
        diary_instance = DiaryEntries.objects.get(pk=DiaryEntries_id)
        diary_instance.highlight = highlight
        diary_instance.diarycontent = diarycontent
        diary_instance.save()
        return redirect(f"/diary/{DiaryEntries_id}/")

    return render(request, "edit_diary.html", {"editdiary":diary_instance,"owner":owner})


def delete_diary(request, DiaryEntries_id):
	delete_diary_instance = DiaryEntries.objects.get(pk=DiaryEntries_id)
	delete_diary_instance.delete()

	return redirect("/dashboard/")


def faq(request):
    return render(request, "faq.html")

def feedback(request):
    user=request.user
    if request.method == "POST":
        number_of_times=request.POST["number_of_times"]
        prefer=request.POST["prefer"]
        user_friendly=request.POST["user_friendly"]

        feedbacks=Feedback.objects.create(
            user=user,
            number_of_times=number_of_times,
            prefer=prefer,
            user_friendly=user_friendly
        )
    return render(request, "feedback.html")

def contact(request):
    return render(request, "contactus.html")

def addToFavourites(request,DiaryEntries_id):
    favDiaries=DiaryEntries.objects.get(pk=DiaryEntries_id)

    if request.method =="POST":
        is_favourite = request.POST["is_favourite"]
        print("h")
        favDiaries=DiaryEntries.objects.get(pk=DiaryEntries_id)
        favDiaries.is_favourite=True
        favDiaries.save()
        return redirect("/dashboard/")
    return redirect("/dashboard/")

def unFavourite(request,DiaryEntries_id):
    unfav=DiaryEntries.objects.get(pk=DiaryEntries_id)
    if request.method =="POST":
        is_favourite = request.POST["is_favourite"]
        print("k")
        unfav=DiaryEntries.objects.get(pk=DiaryEntries_id)

        unfav.is_favourite=False
        unfav.save()
        return redirect("/dashboard/")  
    return redirect("/dashboard/")  

# @login_required
def starred(request):
    user=request.user
    owner=Owner.objects.get(user=user)
    all_diaries=DiaryEntries.objects.filter(is_favourite=True).filter(user=user).order_by('-timestamp')
    return render(request,"starred.html",{"all_diaries":all_diaries, "owner":owner})

# @login_required
def profile(request):
    user=request.user
    owner=Owner.objects.get(user=user)
    if request.method=="POST":
        fullname=request.POST["fullname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        diaryname=request.POST["diaryname"].upper()
        first_name=fullname.split()[0]
        last_name=" ".join(fullname.split()[1:])    
        owner.user.first_name=first_name
        owner.user.last_name=last_name
        owner.user.username=username
        owner.user.email=email
        owner.user.password=password
        owner.diaryname=diaryname 
        owner.save()
        return redirect("/myprofile/")
    messages.success(request,"Your profile was edited successfully")
    return render(request, "profile.html",{"owner":owner})
