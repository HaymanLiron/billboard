from django.shortcuts import render
from django.views import generic
from .models import Message
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm



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


def check_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
            login(request,user)
            return HttpResponseRedirect('/messageboard/')
    else:
        print("The password is valid, but the account has been disabled!")
        form = UserCreationForm()
        return render(request, "registration/register.html", {
            'form': form,
        })





    # the authentication system was unable to verify the username and

    password

    print("The username and password were incorrect.")

#
# def some_view(request):
#
#     if request.user.is_authenticated():
#
#     # Do something for authenticated users.
#
#     else:
#
#     # Do something for anonymous users.
#

