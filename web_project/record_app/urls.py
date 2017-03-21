from django.conf.urls import url, include
from record_app import views

urlpatterns = [
   
    url(r'^$', views.ListPostsView.as_view(), name='list_posts'),
    url(r'^(?P<pk>\d+)/$', views.DetailPostView.as_view(), name='detail_posts'),

]