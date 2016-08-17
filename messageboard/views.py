from django.shortcuts import render
from django.views import generic
from .models import User, Message


class IndexView(generic.ListView):
    template_name = 'messageboard/index.html'
    context_object_name = 'last_messages'

    def get_queryset(self):
        return Message.objects.order_by('-pub_date')[:5]


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



