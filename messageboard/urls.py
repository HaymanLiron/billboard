from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^submit-message$', views.create_message_database, name='submit-message'),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/login$', 'django.contrib.auth.views.login'),
]
