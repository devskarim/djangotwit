from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog 


def home(request): 
	search = request.GET.get('q')

	if search: 
		blog = Blog.objects.filter(title__icontains = search) 
	else: 
		blog = Blog.objects.all()
		
	return render(request, 'index.html', {'blog': blog})


def detail_blog(request,id):
	blog = get_object_or_404(Blog, id=id) 
	context = {
			"blog": blog
		}
	return render(request, 'detail.html', context)


def create_blog(request): 
	if request.method == 'POST':
		title  = request.POST.get('title')
		author = request.POST.get('author')
		desc = request.POST.get('desc')
		image = request.FILES.get('image') 
		is_published =  True if request.POST.get('is_published') == 'on' else False

		Blog.objects.create(
			title= title, author=author, desc = desc, image = image, is_published = is_published
		) 

		return redirect('/')
	return render(request, 'create.html')


def delete_blog(request, id): 
	if request.method == 'POST': 
		blog = get_object_or_404(Blog, id=id) 
		blog.delete()
		return redirect('/')
	return render(request, 'delete.html')

def edit_blog(request, id):

	blog = get_object_or_404(Blog,id=id)

	if request.method == 'POST': 
		blog.title = request.POST.get('title')
		blog.author = request.POST.get('author')
		blog.desc = request.POST.get('desc')
		if request.FILES.get('image'):
			blog.image = request.FILES.get('image') 
		blog.is_published = bool(request.POST.get('is_published'))

		blog.save()

		return redirect('/')
	return render(request,'edit.html', {'blog': blog}) 


def profile_view(request): 

	user = Blog.objects.all()
	context = {
		'user': user
	}

	return render(request, 'profil.html', context)