from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^messageboard/submit-message$', views.submit_message, name='submit-message'),
]
