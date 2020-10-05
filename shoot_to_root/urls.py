from django.urls import path
from shoot_to_root.views import PostList,PostDetail
from . import views

app_name="shoot_to_root"

urlpatterns=[
	path('',views.home,name='homepage'),
	path('contact', views.contact,name='Contact'),
	path('comment', views.comment,name='Comment'),
	path('base.html',views.home,name='homepage'),
	path('blogs.html',PostList.as_view(),name='post-list'),
	path('detail/<int:pk>/',PostDetail.as_view(),name='post-detail')
]