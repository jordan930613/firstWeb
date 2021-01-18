"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from mainsite.views import homepage, showpost

urlpatterns = [
    path('admin/', admin.site.urls),
    # 根目錄(127.0.0.1:8000)
    path('', homepage),
    # 把所有post/開頭的網址後面的字串都找出來傳遞給showpost
    path('post/<slug:slug>', showpost)
]
