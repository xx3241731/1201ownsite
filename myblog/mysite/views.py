#python程式
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post #把在models.py中自定義的Class引入Post資料表
import random
from datetime import datetime
from mysite.models import AccessInfo

# Create your views here.

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all() #取得所有Post 並放入變數posts
    now = datetime.now()       #index.html即可使用datetime
    return render(request,'index.html',locals())#最後需要return

def lotto(request):
    now = datetime.now()
    lucky = random.randint(1,42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1,42))
    return render(request,'lotto.html',locals())

def showpost(request, slug):
    now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        return render(request,'post.html',locals())
    except:
        return redirect('/')

def mychart(request):
    now = datetime.now()
    return render(request, 'mychart.html',locals())

    
   