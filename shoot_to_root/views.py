from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView,DetailView
from shoot_to_root.models import Post,Contact,Comment,CTF

class PostList(ListView):
	model=Post

class PostDetail(DetailView):
	model=Post

class CTFList(ListView):
	model=CTF

class CTFDetail(DetailView):
	model=CTF

def home(request):
	return render(request,'base.html')

def comment(request):
	if request.method=="POST":
		comment1=request.POST["comment"]
		comment_obj=Comment(comments=comment1)
		comment_obj.save()
	return redirect(request.META['HTTP_REFERER'])

def contact(request):
	if request.method=="POST":
		name=request.POST["nm"]
		email=request.POST["em"]
		phone=request.POST["phoneno"]
		comment=request.POST["comment"]
		contacts=Contact(name=name,email=email,phone=phone,comment=comment)
		contacts.save()
	return redirect(request.META['HTTP_REFERER'])
