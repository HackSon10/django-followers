# Imports of Python
import datetime

# Imports of django
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

# My imports
from django.contrib.auth.models import User
from .models import Friend

def index(request):
	reqs = Friend.objects.filter(user_to=request.user, status=1)
	num_reqs = Friend.objects.filter(user_to=request.user, status=1).count()

	reqs_s = Friend.objects.filter(friend_to=request.user, status=1)
	num_reqs_s = Friend.objects.filter(friend_to=request.user, status=1).count()

	friend = Friend.objects.filter(friend_to=request.user, status=2)
	num_friend = Friend.objects.filter(friend_to=request.user, status=2).count()

	data = {
		'requests':reqs,
		'follow':reqs_s,
		'friend':friend,
		'numfriend':num_friend,
		'numreqs':num_reqs_s,
		'numreq':num_reqs,
	}

	res = render(request ,'index.html', data)
	
	return res

def other_user(request, user_id):
	friend = get_object_or_404(User, username=user_id)

	relation = Friend.objects.filter(
	Q(user_to=request.user) & Q(friend_to=friend)|
	Q(user_to=friend) & Q(friend_to=request.user))[:1]

	data = {
		'friend':friend,
		'relation':relation,
	}

	return render(request, 'friend.html', data)

def add_user(request, user_id):
	friend = get_object_or_404(User, username=user_id)

	relation = Friend(user_to=request.user, friend_to=friend, status=1)
	relation.save()

	return redirect('/%s/' % (friend))

def accept_request(request, user_id):
	friend = get_object_or_404(User, username=user_id)

	relation2 = Friend(user_to=request.user, friend_to=friend, status=2)
	relation2.save()

	relation = Friend.objects.filter(
	Q(user_to=request.user) & Q(friend_to=friend) |
	Q(user_to=friend) & Q(friend_to=request.user)).update(status=2)

	return redirect('/')

def reject_request(request, user_id):
	friend = get_object_or_404(User, username=user_id)

	relation = Friend.objects.filter(
	Q(user_to=request.user) & Q(friend_to=friend) |
	Q(user_to=friend) & Q(friend_to=request.user)).delete()

	return redirect('/')









