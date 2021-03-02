from django.shortcuts import render
from hamlet.models import Announcment, Region, District, Status
from django.contrib.auth.models import User
import json
from django.core import serializers
from PIL import Image
from django.core.files.storage import FileSystemStorage

def index(request, username):
    announcements = Announcment.objects.filter(author=username)
    user = User.objects.filter(username=username)
    return render(request, "personal_area/index.html", {'announcements': announcements, 'user': user})


def add(request, username):
    
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    statuses = Status.objects.all()
    # types = Type.objects.all()
    # views = View.objects.all()

    
    if request.method == 'POST' and request.FILES:
        title = request.POST['title']
        # content = request.POST['content']
        region = request.POST['region_id']
        district = request.POST['district_id']
        # address = request.POST['address']
        # type = request.POST['type_id']
        # view = request.POST['view_id']
        status = request.POST['status_id']
        price = request.POST['price']
        features = request.POST['features']
        image = request.FILES.get['image']
        # phone = request.POST['phone']

        announcement = Announcment(
            title=title,
            # content=content,
            region=region,
            district=district,
            # address=address,
            # type=type,
            # view=view,
            status=status,
            price=price,
            features=features,
            image=image,
            # phone=phone,
            author=username
        )
        announcement.save()
    return render(request, 'add.html',
    {
        'regions': regions,
        'districts': districts,
        'statuses': statuses,
        # 'types': types,
        # 'views': views
    })