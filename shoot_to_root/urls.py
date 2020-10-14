from django.urls import path
from shoot_to_root.views import PostList,PostDetail,CTFList,CTFDetail
from . import views

app_name="shoot_to_root"

urlpatterns=[
	path('',views.home,name='homepage'),
	path('contact', views.contact,name='Contact'),
	path('comment', views.comment,name='Comment'),
	path('flag_submit', views.flag,name='flag_submit'),
	path('ctfs.html',CTFList.as_view(),name='ctf-list'),
	path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
	path('ctf/<int:pk>/',CTFDetail.as_view(),name='ctf-detail'),
	path('base.html',views.home,name='homepage'),
	path('blogs.html',PostList.as_view(),name='post-list')
]