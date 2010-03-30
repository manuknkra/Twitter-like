# Create your views here.
from django.shortcuts import render_to_response
from models import *
from django import forms
from django.contrib.auth.models import User
from twitter.views import Follow

def UserPage(request, username):
	user_account  = account.objects.get(username=username)
	tweets = user_account.tweets.order_by('-id')
	if request.method == 'POST':
		Follow(username)

	return render_to_response('user_page.html',{'tweets':tweets,'username':username})

def UserFollowing(request, username):
	user_account = account.objects.get(username = username)
	following_list = user_account.following.all()
	return render_to_response('user_following.html',{'following_list':following_list})

def UserFollowers(request, username):
	user_account = account.objects.get(username = username)
	followers = user_account.followers.all()
	return render_to_response('user_followers.html',{'followers':followers})
