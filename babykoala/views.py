
from django.shortcuts import render

def post_list(request):
    return render(request, 'babykoala/post_list.html', {})
