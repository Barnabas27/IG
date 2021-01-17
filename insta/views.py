from django.shortcuts import render, redirect
from .forms import ProfileForm,ImageForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Picture, Profile,Comments,Likes
from vote.managers import VotableManager

votes = VotableManager()


# Create your views here.
# def home(request):
#     return render(request,'')
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    posts = Picture.get_all_images()
    comments = Comments.objects.all()
    profile = Profile.get_all_profiles()
    
    return render(request,'insta/home.html',locals())

@login_required(login_url='/accounts/login/')
def add_image(request):
        current_user = request.user
        if request.method == 'POST':
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('home')
        else:
                form = ImageForm()
                return render(request,'insta/image.html', {"form":form})
            

@login_required(login_url = '/accounts/login/')
def profile_info(request):
        current_user = request.user
        profile = Profile.objects.filter(user=current_user).first()
        posts = request.user.image_set.all()
        
        return render(request,'insta/profile.html',{"images":posts,"profile":profile})
    
@login_required(login_url='/accounts/login/') 
def profile_update(request):
         current_user = request.user
         if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('profile')
         else:
                form = ProfileForm()
         return render(request,'instagram/profile_update.html',{"form":form})

@login_required(login_url='/accounts/login/') 
def comment(request,image_id):
        current_user=request.user
        image = Picture.objects.get(id=image_id)
        profile_owner = User.objects.get(username=current_user.username)
        comments = Comments.objects.all()
        
        if request.method == 'POST':
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.image = image
                        comment.user = request.user
                        comment.save()
            
                       
                return redirect('index')
        else:
                form = CommentForm()
        return render(request, 'instagram/comment.html',locals())