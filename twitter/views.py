from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from profiles.models import *

HOME_USER = ''

class UserForm(forms.Form):
	UserName = forms.CharField(30)
	Password = forms.CharField(30,widget=forms.PasswordInput)

class TweetForm(forms.Form):
        wassup = forms.CharField(140)

def LogIn(request):
	form = UserForm()
	errors = []
	Username = "" 
	flag = 0
	if request.method == 'POST':
		if not request.POST.get('UserName',''):
			errors.append("* Enter the Username")
		if not request.POST.get('Password',''):
			errors.append("* Enter the Password")
		if not errors:
			Username =request.POST['UserName']
			Password =request.POST['Password']
			global HOME_USER
			HOME_USER = auth.authenticate(username=Username, password=Password)
			if HOME_USER is not None and HOME_USER.is_active:
        # Correct password, and the user is marked "active"
			        auth.login(request, HOME_USER)
        # Redirect to a success page.
				return HttpResponseRedirect("/home_page/")
			else:
				errors.append("Wrong Username or Password")
	
	return render_to_response('login.html',{'form':form,'Username':Username,'errors':errors})

def HomePage(request):
        username = HOME_USER.username
        user_account  = account.objects.get(username=username)
        #tweets = user_account.tweets.order_by('-id')
        form = TweetForm()


        if request.method == 'POST':
                if request.POST.get('wassup',''):
                        message = request.POST['wassup']
                	new_tweet = Tweet.objects.create(message = message)
                	user_account.tweets.add(new_tweet)
	
	tweets = TweetUpdate(user_account)[0]
	tweets_by = TweetUpdate(user_account)[1]

        return render_to_response('home_page.html',{'tweets':tweets,'tweets_by':tweets_by,'form':form,'username':username})

def TweetUpdate(user_account):
	tweet_data_list = []
	for tweet in user_account.tweets.all():
		tweet_data_list.append([tweet.id, user_account.username])
	for following in user_account.following.all():
		following_account = account.objects.get(username = following.username)
		following_tweets = following_account.tweets.all()
		for following_tweet in following_tweets:
			tweet_data_list.append([following_tweet.id, following.username])
	tweet_data_list.sort(reverse = True)
	
	tweets = []
	tweets_by = []
	for tweet_data in tweet_data_list:
		tweets.append(Tweet.objects.get(id = tweet_data[0]))
		tweets_by.append(tweet_data[1])
	return tweets,tweets_by

def Follow(username):
	#print HOME_USER.username + "following" + username
	home_user_account = account.objects.get(username = HOME_USER.username)
	user_account = account.objects.get(username = username)
	
	followers_username = Follower.objects.get(username = HOME_USER.username)
	user_account.followers.add(followers_username)
	
	following_username = Following.objects.get(username = username)
	home_user_account.following.add(following_username)

def LogOut(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login/")
