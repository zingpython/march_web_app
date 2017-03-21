from django.shortcuts import render
from django.views.generic.list import ListView
from record_app.models import Post



class ListPostsView(ListView):

    model = Post
