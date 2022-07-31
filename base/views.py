from django.shortcuts import render, redirect, get_object_or_404
from .forms import registerform, revform, aboutform
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib import messages

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    form = revform()
    pal = list(aboutmovie.objects.all())
    allo = aboutmovie.objects.all().count()
    all = random.sample(pal, allo)
    return render(request, "base/home.html", {
        'all': all,
        'form': form
    })

def update(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    fun = aboutmovie.objects.get(id=pk)
    fun.done = True
    fun.save()
    return HttpResponseRedirect(reverse("home"))

def disupdate(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    fun = aboutmovie.objects.get(id=pk)
    fun.done = False
    fun.save()
    return HttpResponseRedirect(reverse("home"))

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    people = request.user
    all = aboutmovie.objects.filter(user=people)
    form = revform()
    return render(request, "base/profile.html", {
        'all': all,
        'form': form
    })

def started(request):
    return render(request, "base/started.html", {})
    
def sec(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    peo = request.user
    all = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    form = aboutform()
    return render(request, "base/sec.html", {
        'all': all,
        'form': form
    })

def startsec(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    peo = request.user
    message = "hi"
    if request.method == 'POST':
        form = aboutform(request.POST, request.FILES)
        if form.is_valid():
            fore = form.save(commit=False)
            fore.user = peo
            win = form.cleaned_data['description']
            fore.description = win
            fore.save()
            posts = get_object_or_404(movieimg, id=request.POST.get('all_id'))
            fore.image.add(posts)
            return HttpResponseRedirect(reverse("home"))
        else:
            form = aboutform()
    return HttpResponseRedirect(reverse("home"))
            

def create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    if request.method == "POST":
        per = request.user
        image = request.FILES['image']
        dud = movieimg(user=per, img=image)
        dud.save()
        return HttpResponseRedirect(reverse("sec"))
    return render(request, "base/create.html", {})
    
def about(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    alle = aboutmovie.objects.get(id=pk)
    adds = alle.review_set.all().order_by('-id')
    if request.method == "POST":
        form = revform(request.POST, instance=alle)
        if form.is_valid():
            body = form.cleaned_data['comment']
            log = request.user
            c = review(join=alle, comment=body, person=log)
            c.save()
       
    else:
        form = revform()
    return render(request, "base/about.html", {
        'all': alle,
        'form': form,
        'adds': adds
    })
    
def area(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    feed = aboutmovie.objects.get(id=pk)
    adds = feed.review_set.all()
    if request.method == "POST":
        form = revform(request.POST, instance=feed)
        if form.is_valid():
            body = form.cleaned_data['comment']
            log = request.user
            c = review(join=feed, comment=body, person=log)
            c.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            form = revform()
    return HttpResponseRedirect(reverse("home"))
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "base/login.html", {
            "massage": "invalid credentials"
            })
    return render(request, "base/login.html", {})

def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = registerform()
        #messages.debug(request, '%s SQL statements were executed.' % count)
        #messages.info(request, 'Three credits remain in your account.')
        #messages.success(request, 'Profile details updated.')
        #messages.warning(request, 'Your account expires in three days.')
        #messages.error(request, 'There was an Error in Signing you Up.')
    return render(request, "base/register.html", {
        'form': form
    })
    
def logout_view(request):
    logout(request)
    return render(request, "base/login.html", {
    "message":"Logged out"
    })