from pydoc import describe
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Video
from django.utils.timezone import now


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