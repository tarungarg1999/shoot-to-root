from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView,DetailView
from shoot_to_root.models import Post,Contact,Comment

class PostList(ListView):
	model=Post

class PostDetail(DetailView):
	model=Post

def home(request):
	return render(request,'base.html')

def comment(request):
	if request.method=="POST":
		comment1=request.POST["comment"]
		comment_obj=Comment(comments=comment1)
		comment_obj.save()
	return render(request,'base.html')

def contact(request):
	if request.method=="POST":
		name=request.POST["nm"]
		email=request.POST["em"]
		phone=request.POST["phoneno"]
		comment=request.POST["comment"]
		contacts=Contact(name=name,email=email,phone=phone,comment=comment)
		contacts.save()
	return render(request,'base.html')
