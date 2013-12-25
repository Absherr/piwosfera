# Create your views here.
from httplib import HTTP
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from main.models import *
from django.utils import timezone
from datetime import timedelta

# def readable_delta(dt):
# 	now = timezone.now()
# 	delta = now - timezone.make_aware(dt, timezone.get_default_timezone())
	
# 	if delta.days == 0:
# 		seconds = delta.seconds
# 		if seconds < 60:
# 			return "Przed chwila"
# 		elif seconds<3600:
# 			return str(seconds/60) + " minut temu"
# 		else:
# 			hours = seconds/3600
# 			if hours in (1,):
# 				return str(hours) + " godzine temu"
# 			if hours in (2, 3, 4):
# 				return str(hours) + " godziny temu"
# 			if hours in range(5, 25):
# 				return str(hours) + " godzin temu"
				
# 	if delta.days == 1:
# 		return "Wczoraj"
# 	if delta.days >= 2:
# 		return str(delta.days) + " dni temu"
# 	return delta.seconds/3600
# 	# if delta > timedelta(days=7):
# 	# 	return "Ponad tydzien temu"
# 	# if delta > timedelta(days=6):
# 	# 	return "7 dni temu"
# 	# if delta > timedelta(days=5):
# 	# 	return "6 dni temu"
# 	# if delta > timedelta(days=4):
# 	# 	return "5 dni temu"
# 	# if delta > timedelta(days=3):
# 	# 	return "4 dni temu"
# 	# if delta > timedelta(days=2):
# 	# 	return "3 dni temu"
# 	# if delta > timedelta(days=1):
# 	# 	return "2 dni temu"
# 	# if delta > timedelta(days=0):
# 	# 	return "1 dni temu"
	
	
	# return delta

def home_view(request):
    entries = Entry.objects.all()[:40]
    blogs = Blog.objects.all().order_by('name')

    # for entry in entries:
    # 	entry.delta = readable_delta(entry.date) 

    return render_to_response("home.html",{'entries':entries,'blogs':blogs})


# def blog_add_popularity(request, blog_id=""):
#     if blog_id=="":
#         return HttpResponseRedirect("/")
#     b = Blog.objects.filter(id=blog_id)[0]
#     b.popularity+=1
#     b.save()

#     return HttpResponseRedirect(b.address)

# def entry_add_popularity(request, entry_id=""):
#     if entry_id=="":
#         return HttpResponseRedirect("/")
#     e = Entry.objects.filter(id=entry_id)[0]
#     e.popularity+=1
#     e.save()

#     b = Blog.objects.filter(id=e.blog_id)[0]
#     b.popularity+=1
#     b.save()

#     return HttpResponseRedirect(e.address)