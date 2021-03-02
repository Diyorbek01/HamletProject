from django.shortcuts import render, redirect
from .models import Announcment
from django.core.mail import send_mail
from .models import SubscribedUser
from .forms import SubscribeForm

def index(request):
    announcements = Announcment.objects.all()
    if request.method == 'POST':
        s_form = SubscribeForm(request.POST)
        if s_form.is_valid():
            email = s_form.cleaned_data['subscribe']

            send_mail(
                'Joined successfully',
                'You are joined successfully! Enjoy with us.'
                'diyorbeky610@gmail.com',
                [email],
                fail_silently=False
            )

            subscribed_user = SubscribedUser(email=email)
            subscribed_user.save()
    else:
        s_form = SubscribeForm()
    return render(request, "index.html", {'announcements': announcements, 's_form': s_form})


def about(request):
    if request.method == 'GET':
        s_form = SubscribeForm(request.GET)
        if s_form.is_valid():
            email = s_form.cleaned_data['subscribe']

            send_mail(
                'Joined successfully',
                'You are joined successfully! Enjoy with us.'
                'testingemail286@gmail.com',
                [email],
                fail_silently=False
            )

            subscribed_user = SubscribedUser(email=email)
            subscribed_user.save()
    else:
        s_form = SubscribeForm()
    return render(request, "about.html", {'s_form': s_form})


def contact(request):
    if request.method == 'GET':
        s_form = SubscribeForm(request.GET)
        if s_form.is_valid():
            email = s_form.cleaned_data['subscribe']

            send_mail(
                'Joined successfully',
                'You are joined successfully! Enjoy with us.'
                'testingemail286@gmail.com',
                [email],
                fail_silently=False
            )

            subscribed_user = SubscribedUser(email=email)
            subscribed_user.save()
    else:
        s_form = SubscribeForm()
    return render(request, "contact.html", {'s_form': s_form})


def blog(request):
    if request.method == 'GET':
        s_form = SubscribeForm(request.GET)
        if s_form.is_valid():
            email = s_form.cleaned_data['subscribe']

            send_mail(
                'Joined successfully',
                'You are joined successfully! Enjoy with us.'
                'testingemail286@gmail.com',
                [email],
                fail_silently=False
            )

            subscribed_user = SubscribedUser(email=email)
            subscribed_user.save()
    else:
        s_form = SubscribeForm()
    return render(request, "blog.html", {'s_form': s_form})

def agents(request):
    if request.method == 'GET':
        s_form = SubscribeForm(request.GET)
        if s_form.is_valid():
            email = s_form.cleaned_data['subscribe']

            send_mail(
                'Joined successfully',
                'You are joined successfully! Enjoy with us.'
                'testingemail286@gmail.com',
                [email],
                fail_silently=False
            )

            subscribed_user = SubscribedUser(email=email)
            subscribed_user.save()
    else:
        s_form = SubscribeForm()
    return render(request, "agents.html", {'s_form': s_form})

def properties(request):
    if request.method == 'GET':
        s_form = SubscribeForm(request.GET)
        if s_form.is_valid():
            email = s_form.cleaned_data['subscribe']

            send_mail(
                'Joined successfully',
                'You are joined successfully! Enjoy with us.'
                'testingemail286@gmail.com',
                [email],
                fail_silently=False
            )

            subscribed_user = SubscribedUser(email=email)
            subscribed_user.save()
    else:
        s_form = SubscribeForm()
    return render(request, "properties.html", {'s_form': s_form})