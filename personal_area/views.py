from django.shortcuts import render
# from hamlet.models import Announcment
# from django.contrib.auth.models import User

def index(request, username):
    # announcments = Announcment.objects.filter(author=username)
    # user = User.objects.filter(username=username)
    return render(request, "index.html"
    # , {'announcments': announcments, 'user': user}
    )
