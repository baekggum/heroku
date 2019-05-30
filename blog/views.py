from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth
# Create your views here.
def blog(request):#blog 함수임
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})#python 변수를 html에서 쓸꺼야

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)#객체를 줘 어떤 클래스에 blog_id와 관련된 객체를
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')#화면에 new.html을 띄워죠

def create(request):
    blog = Blog()
    blog.title = request.GET['title']#받은 변수 사용하기
    blog.body = request.GET['body']
    blog.pub_date = timezone.now()
    blog.save()
    return redirect('/detail/'+str(blog.id))#해당되는 url을 시작해줘

def login(request):
    if request.method == "POST":#보안에 신경 썼니?
        user = auth.authenticate(request, username = request.POST['username'], password = request.POST['password'])#존재하니?
        if user is not None:
            auth.login(request, user)#로그인
            return redirect('blog')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])#유저 만들어줘
                auth.login(request, user)#유저 로그인해줘
                return redirect('blog')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'signup.html')