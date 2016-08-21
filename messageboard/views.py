from django.shortcuts import render
from django.views import generic
from .models import Message
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'messageboard/index.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        return Message.objects.order_by('-pub_date')[:5]


def create_message_database(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    message_text = request.POST.get('text')

    new_msg = Message(user_name=author, title=title,
                             text=message_text, pub_date=timezone.now())
    new_msg.save()

    return HttpResponseRedirect("/messageboard")


