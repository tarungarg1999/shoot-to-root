from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView,DetailView
from shoot_to_root.models import Post,Contact,Comment,CTF,Flag

class PostList(ListView):
	model=Post

class PostDetail(DetailView):
	model=Post
	
class CTFList(ListView):
	model=CTF

	# def __init__(self):
	# 	model1=CTF.objects.get(id=1)
	# 	model1.index=1
	# 	model1.save()

class CTFDetail(DetailView):
	model=CTF

def home(request):
	return render(request,'base.html')
def about(request):
	return render(request,'about.html')

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
		#phone=request.POST["phoneno"]
		comment=request.POST["comment"]
		contacts=Contact(name=name,email=email,comment=comment)
		contacts.save()
	return redirect(request.META['HTTP_REFERER'])

def flag(request):
	if request.method=="POST":
		flag_submit=request.POST["flag"]
		index=request.POST["index"]
		category=request.POST["cate"]
		flag_obj=CTF.objects.get(id=1)
		real_flag=flag_obj.flag
		if real_flag==flag_submit:
			flag_obj.index=10
			flag_obj.save()
			result="Well Done, you got the Right flag :)"
			#print(result,i)
			#return HttpResponseRedirect(request.META.get('HTTP_REFERER'),{result:'result'})
			#return render(request,'base.html',{result:'result'})
			return redirect(request.META['HTTP_REFERER'])
		else:
			result="Try again !!!"
			flag_obj.index=12
			flag_obj.save()
			#print(result,request.META['HTTP_REFERER'],i)
			#return HttpResponseRedirect(request.META.get('HTTP_REFERER'),{result:'result'})
			#return render(request,'base.html',{result:'result'})
			return redirect(request.META['HTTP_REFERER'])
		#flag_obj=Flag(flag=flag_submit)
		#flag_obj.save()
	#return redirect(request.META['HTTP_REFERER'])
