from django.shortcuts import render

def index(request):
    context = {
        'title': 'Welcome to My App',
        'message': 'Successfully deployed with Docker and GitHub Actions!',
    }
    return render(request, 'home/index.html', context)
