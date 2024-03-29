﻿from django.shortcuts import render, redirect
from .models import * 
from .forms import ContactForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView, View
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from django.conf import settings

bad_words = ['арбуз']

def index(request):
    ad = book.objects.all()
    genre = genre_of_the_book.objects.all()


    context ={
        'ad':ad,
        'genre':genre,
        }
    return render(request,'main/index.html',context = context)

def ad_info(request, ad_id):
    ad = book.objects.filter(id = ad_id)
    search_book = book.objects.get(id = ad_id)
    comment = comment_book.objects.filter(book_in_comment = ad_id)
    text = request.POST.get('Text')
    if str(text).replace(" ", "") == '':
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if request.method == "POST":
        for word in text.lower().split():
            if word in bad_words:
                comment_book.objects.create(is_publishe = False, author = request.user,text = request.POST.get('Text'),book_in_comment=search_book)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        comment_book.objects.create(author = request.user,text = text,book_in_comment=search_book)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context ={
        'ad':ad,
        'comment':comment,
        }
    return render(request,'main/ad.html',context = context)



def home(request):
    p = {}
    select = selection_book.objects.all()

    for s in select:
        b = book.objects.filter(genre = s.genre).order_by("-id")[0:4]
        if b:
            p[s] = b
    context = {
        "books":book.objects.all().order_by("-id")[0:4],
        "author":Author_of_the_book.objects.all().order_by("-id")[0:4],
        "selection_book":p,
        "select":select,
        }

    return render(request,'main/home.html',context = context)

def profile_user(request,pk):
    user = User.objects.filter(pk = pk)
    p = profile.objects.filter(user = User.objects.get(pk = pk))
    context ={
        'profile':p,
        'user':user
        }
    return render(request,"main/profile.html",context = context)

from django.http import HttpResponse, HttpResponseRedirect


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = EmailMessage(form.cleaned_data['subject'], form.cleaned_data['message'], to=['egor-karpov09@bk.ru'])
            email.send()


    form = ContactForm()
    return render(request,"main/contact.html", {'form': form})


class edit_profile(UpdateView):
    model = User
    template_name = 'main/porfile.html'

    fields = ['username', 'last_name', 'first_name', 'email']

def comments(request):
    if request.method == "POST":
        comment_book.objects.create(author = request.user,text = request.POST.get('Text'),book_in_comment=search_book)
    return redirect(request.path)

def delete_comment(request):
    if request.method == 'POST':
        comment_id = request.GET.get('comment_id')
        find_comment = comment_book.objects.get(id = comment_id)
        find_comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def public_comment(request):
    if request.method == 'POST':
        comment_id = request.GET.get('comment_id')
        find_comment = comment_book.objects.get(id = comment_id)
        find_comment.is_publishe = True
        find_comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


