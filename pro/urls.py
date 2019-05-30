"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import blog.views#블로그안에 있는 views라는 파이썬 파일을 가져옴

from django.conf import settings#내 세팅을 가져와라
from django.conf.urls.static import static#url들을 가져와라

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.blog, name = "blog"),#url이 ''이면 blog 함수를 실행 시켜라. 이름은 blog다.
    path('detail/<int:blog_id>/', blog.views.detail, name = "detail"),#나는 blog_id도 같이 받을꺼다.
    path('new/',blog.views.new, name="new"),
    path('create/',blog.views.create, name="create"),#함수 실행이 주 목적임
    path('login/', blog.views.login, name ="login"),
    path('signup/', blog.views.signup, name = "signup"),
    path('logout/', blog.views.logout, name ="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#새로운 static을 만들어라 경로는 media고 파일경로는 media 경로다
