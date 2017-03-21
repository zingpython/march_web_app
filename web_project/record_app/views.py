from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from record_app.models import Post



class ListPostsView(ListView):

    model = Post



class DetailPostView(DetailView):

	model = Post

	