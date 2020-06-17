"""djangobasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blogs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('foropen/',views.foropen),
    path('foropen2/',views.foropen2),
    path('foropen3/',views.foropen3),
    path('form/',views.form),
    path('form1_1/',views.form1_1),
    path('form2/',views.form2),
    path('form2_1/',views.form2_1),
    path('form3/',views.form3),
    path('form3_1/',views.form3_1),
    path('form4/',views.form4),
    path('addForm/',views.addBlog),
    path('addForm1_1/',views.addBlog1_1),
    path('addForm2/',views.addBlog2),
    path('addForm2_1/',views.addBlog2_1),
    path('addCustom/',views.addCustom),
    path('viewDev/',views.viewDev)

]

