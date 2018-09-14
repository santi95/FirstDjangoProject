from django.shortcuts import redirect, render
from .models import Comment
import datetime


def index(request):
    comments = Comment.objects.all()
    context = {'comments': comments}

    return render(request, 'tarea1/index.html', context)

def create(request):
    comment = Comment(comment = request.POST['comment'],
                      ip_address = request.environ['REMOTE_ADDR'],
                      date = datetime.datetime.now().strftime("%Y-%m-%d"))
    comment.save()
    return redirect('/')