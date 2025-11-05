from django.urls import path, include
from .views import home, create_blog, delete_blog,edit_blog, detail_blog, profile_view

urlpatterns = [
	path('',home),
	path('create/', create_blog, name='create_blog'),
	path('delete/<int:id>/', delete_blog, name='delete_blog'),
	path('edit/<int:id>', edit_blog, name='edit_blog'),
	path('detail/<int:id>', detail_blog, name='detail_blog'),
	path('profle/', profile_view, name='profile_view')
]
