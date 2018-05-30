
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import SignUpForm, saveProfile
from django.contrib.auth.models import User
from .models import userProfile,Channel, Videos, Subscriber, Watch, Likes
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
	post = userProfile.objects.filter(uname=request.user.id)
	form = Videos.objects.order_by('-pub_date')
	vid=Videos.objects.order_by('-views')
	lists=Channel.objects.order_by('-pub_date')
	return render(request, 'index.html',{'post':post, 'form':form,'vid':vid,'lists':lists })

def getVideos(request, vid):
	post=userProfile.objects.filter(uname=request.user.id)
	form=Videos.objects.filter(id=vid)
	viewsv=Videos.objects.order_by('-views')

	for f in form:
			gets=Channel.objects.filter(name=f.name)

	if 'Sub'in request.POST or 'Like' in request.POST or 'dislike' in request.POST:
		return redirect('login')

	return render(request,'videos1.html',{'post':post, 'form':form,'gets':gets,'viewsv':viewsv})

def videos(request, vid):
	post=userProfile.objects.filter(uname=request.user.id)
	u=get_object_or_404(User, username=request.user.username)
	form=Videos.objects.filter(id=vid)
	viewsv=Videos.objects.order_by('-views')
	if request.user.is_authenticated:
		for f in form:
			gets=Channel.objects.filter(name=f.name)
			c=Videos.objects.get(id=f.id)
			d=f.name
			if f.id==vid and request.user.is_authenticated:
				if Watch.objects.filter(viewsid=c):
					messages.add_message(request, messages.ERROR, 'You already view')
				else:
					f.views=f.views+1
					f.save()
					watchobj=Watch.objects.create(user=u, viewsid=c)

		title=Channel.objects.filter(name=d)
		for t in title:
			subs=Videos.objects.filter(name=t.id)
			x=t.id
			if 'Sub' in request.POST:
				t.subscribe=t.subscribe+1
				t.save()
			if 'unSub' in request.POST:
				t.subscribe=t.subscribe-1
				t.save()
		for f in form:
			c=Videos.objects.get(id=f.id)
			if 'Like' in request.POST:
				f.like=f.like+1
				f.save()
				likesobj=Likes.objects.create(user=u, likesid=c)

			if 'dislike' in request.POST:
				f.dislike=f.dislike+1
				f.save()

		if request.POST and 'Sub' in request.POST:
			user=u
			name=Channel.objects.get(name=d)
			if Subscriber.objects.filter(sub_name=x).exists():
				messages.add_message(request, messages.ERROR, 'You have alredy subscribe this channel.')
			else:
				subsobj=Subscriber.objects.create(user=user, sub_name=x)

		if request.POST and 'unSub' in request.POST:
			lists=Subscriber.objects.filter(sub_name=x)
			for l in lists:
				if l.sub_name==x:
					l.delete()
		tests=Subscriber.objects.filter(sub_name=x)

	return render(request,'videos.html',{'post':post, 'form':form,'gets':gets,'tests':tests,'viewsv':viewsv})

def  getRegister(request):
	form=SignUpForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, 'Registration Successfully Completed!')
		return redirect('login')
	return render(request, 'signup.html',{'form':form})

def getLogin(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method=='POST':
			user = request.POST.get('user')
			password=request.POST.get('pass1')
			auth=authenticate(request,username=user,password=password)
			if auth is not None:
				login(request, auth)
				return redirect('index')
			else:
				messages.add_message(request, messages.ERROR, 'Incorrect username or password.')
	return render(request,'login.html')

def getLogout(request):
	logout(request)
	return render(request,'logout.html')

def getProfile(request):
	new=userProfile.objects.filter(uname=request.user.id)
	u=get_object_or_404(User, username=request.user.username)
	form=saveProfile(request.POST or None, request.FILES or None)
	if form.is_valid():
		if userProfile.objects.filter(uname=request.user.id).exists():
			messages.add_message(request, messages.ERROR, 'You already saved your information. If wants to modify just click update button.')
		else:
			instance=form.save(commit=False)
			instance.uname=u
			instance.save()
			return redirect('userprofile')
	return render(request, 'profile.html', { 'form':form,'new':new })

def setProfile(request):
	post = userProfile.objects.filter(uname=request.user.id)
	context={'post':post}
	return render(request, 'showProfile.html', context)

def myChannel(request):
	new=userProfile.objects.filter(uname=request.user.id)
	post=Channel.objects.filter(user=request.user.id)
	context={'new':new, 'post':post}
	return render(request, 'mychannel.html', context)

def createChannel(request):
	new=userProfile.objects.filter(uname=request.user.id)
	u=get_object_or_404(User, username=request.user.username)
	if request.POST:
		user=u
		name=request.POST.get('name')
		tag=request.POST.get('tags')
		img=request.FILES.get('file')
		channel_obj=Channel.objects.create(user=user,name=name,tag_line=tag, img=img)
	return render(request, 'newchannel.html',{'new':new})

def setUpload(request):
	new=userProfile.objects.filter(uname=request.user.id)
	form=Channel.objects.filter(user=request.user)
	for f in form:
		cid=f.name
	u=get_object_or_404(User, username=request.user.username)
	c=Channel.objects.get(name=cid)
	if request.POST:
		user=u
		name=c
		title=request.POST.get('name')
		desc=request.POST.get('tags')
		cat=request.POST.get('cat')
		video=request.FILES.get('file')
		img=request.FILES.get('imgfile')
		video_obj=Videos.objects.create(user=user,name=name,title=title, description=desc, category=cat, video=video, img=img)
		return redirect('mychannel')
	return render(request, 'upload.html',{'new':new,'form':form})

def getChannel(request, cid):
	post=userProfile.objects.filter(uname=request.user.id)
	title=Channel.objects.filter(user=request.user.id)
	form=Videos.objects.filter(name=cid)
	return render(request, 'channel.html', {'post':post, 'form':form,'title':title})

def showChannel(request, name):
	u=get_object_or_404(User, username=request.user.username)
	post=userProfile.objects.filter(uname=request.user.id)
	title=Channel.objects.filter(name=name)
	for t in title:
		form=Videos.objects.filter(name=t.id)
		c=t.id
		if 'Sub' in request.POST:
			t.subscribe=t.subscribe+1
			t.save()
		if 'unSub' in request.POST:
			t.subscribe=t.subscribe-1
			t.save()

	if request.POST and 'Sub' in request.POST:
		user=u
		name=Channel.objects.get( name=name)
		if Subscriber.objects.filter(sub_name=name).exists():
			messages.add_message(request, messages.ERROR, 'You have alredy subscribe this channel.')
		else:
			subsobj=Subscriber.objects.create(user=user, sub_name=name)


	if request.POST and 'unSub' in request.POST:
		lists=Subscriber.objects.filter(sub_name=c)
		for l in lists:
			if l.sub_name==c:
				l.delete()
	gets=Subscriber.objects.filter(sub_name=c)
	context={'post':post,'title':title, 'form':form,'gets':gets}
	return render(request, 'showChannel.html',context)

def setSubscribe(request):
	post=userProfile.objects.filter(uname=request.user.id)
	form=Channel.objects.filter(user=request.user.id)
	new=Subscriber.objects.filter(user=request.user.id)
	for n in new:
		gets=Channel.objects.filter(name=n.sub_name)
	context={'post':post,'form':form,'gets':gets}
	return render(request, 'subscribe.html', context)