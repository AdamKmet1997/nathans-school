from pydoc import describe
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Video, User
from django.views.decorators.csrf import csrf_exempt 
from django.utils.timezone import now
from django.contrib.auth import authenticate, login
# @csrf_exempt 
# def login(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         user = User.objects.filter(email=email,password=password)
#         print(user)
#         if user:
#             return HttpResponseRedirect(reverse(index))
#         else:
#             return HttpResponseRedirect(reverse(login))

#     return render(request,"library/login.html")

@csrf_exempt 
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        context["username"] = user
        if user is not None:
            login( request,user)
            #TODO this should go to home poge (redirect) so the url changes instead of 
            #staying on the account/logins page with home.html as template
            return render(request, "home.html",context)
        else:
            #TODO fix this instead of 404 display some message when wrong user name is paassed or password
            raise Http404()

    return render(request, "authentication/login.html",context)

@csrf_exempt 
def signup(request):
    if request.method == "POST":
        username = request.POST.get("nusernameame")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create(username=username,email=email,password=password)

        return HttpResponseRedirect(reverse(login))

    return render(request,"library/signup.html")

def index(request):
    videos = Video.objects.filter(added__lte=now())
    context={"video":videos}
    # print(videos)
    return render(request,"library/index.html",context)

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        url = request.POST.get("url")

        Video.objects.create(title=title,description=description,url=url)

        return HttpResponseRedirect(reverse(index))

    return render(request,"library/add_video.html")

def delete(request,id):
    video = Video.objects.get(id=id)
    video.delete()
    return HttpResponseRedirect(reverse(index))