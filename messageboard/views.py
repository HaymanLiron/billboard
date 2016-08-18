from django.shortcuts import render
from django.views import generic
from .models import Message
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'messageboard/index.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        return Message.objects.order_by('-pub_date')[:2]


def create_message_database(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    message_text = request.POST.get('text')

    new_msg = Message(user_name=author, title=title,
                             text=message_text, pub_date=timezone.now())
    new_msg.save()

    return HttpResponseRedirect("/messageboard")


# def submit_message(request):
#     message=get_object_or404(message,pK=???)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



