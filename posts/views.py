from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Posts.objects.get(id=pk)
    texts = posts.body.split('  ')
    return render(request, 'posts.html', {'posts':posts, 'texts':texts})