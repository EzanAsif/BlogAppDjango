from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def article_list (request) : 
    articles = Article.objects.all().order_by('date') #error faltu mien arha ha
    return render(request, 'articles/article_list.html', {'articles':articles})


def article_detail(request, slug): 
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})



@login_required(login_url = "/accounts/login/") #protecting this user to login will first check if the user is logged in or not
def article_create(request) : 
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #saving the article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})