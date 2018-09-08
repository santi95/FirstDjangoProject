from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Comment
from django.template.loader import render_to_string


def index(request):
    comments = Comment.objects.all()
    context = {'comments': comments}

    return render(request, 'tarea1/index.html', context)

def create(request):
    comment = Comment(comment = request.POST['comment'], ip_address = request.environ['REMOTE_ADDR'])
    comment.save()
    return redirect('/')