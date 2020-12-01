
from django.contrib import admin
from django.urls import path
from mysite.views import homepage,lotto,showpost,mychart

urlpatterns = [
    path('', homepage),
    path('lotto/',lotto),#連結設置好後 在第4行引入lotto 並到views去define
    path('admin/', admin.site.urls),
    path('post/<str:slug>/', showpost),
    path('mychart/', mychart),
    
]
