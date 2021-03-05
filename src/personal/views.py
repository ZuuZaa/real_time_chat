from django.shortcuts import render

def home_screen_view(request, *args, **kwargs):
    context = {}
    return render(request, 'personal/index.html', context)
