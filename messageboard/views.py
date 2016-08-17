from django.shortcuts import render
from django.views import generic
from .models import User, Message


class IndexView(generic.ListView):
    template_name = 'messageboard/index.html'
    context_object_name = 'last_messages'

    def get_queryset(self):
        return Message.objects.order_by('-pub_date')[:5]
