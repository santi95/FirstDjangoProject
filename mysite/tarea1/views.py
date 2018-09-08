from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from django.template.loader import render_to_string


def index(request):
    all_comments = Comment.objects.all()

    objects = {
        'all_comments': all_comments
    }
    message = render_to_string('tarea1/index.html', objects)

    return HttpResponse(message)
