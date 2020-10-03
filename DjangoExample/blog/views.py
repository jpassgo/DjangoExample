from django.shortcuts import render

posts = [
    {
        'author': 'Tiger Woulds',
        'title': 'Blog Post 1', 
        'content': 'First blog post', 
        'date_posted': 'October 3rd 2020' 
    }, 
    {
        'author': 'Michael Cane',
        'title': 'Blog Post 2', 
        'content': 'Second blog post', 
        'date_posted': 'October 3rd 2020' 
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})