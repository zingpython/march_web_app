from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from record_app.models import Post



class ListPostsView(ListView):

	model = Post



class DetailPostView(DetailView):

	model = Post


class CreateRecordView(CreateView):

	model = Post

	fields = ['title', 'slug', 'content', 'image']

class UpdateRecordView(UpdateView):
	model = Post
	fields = ['title', 'content', 'image']
	template_name_suffix = '_update_form'

class DeletePostView(DeleteView):
	model = Post
	success_url = reverse_lazy('records:list_posts')











	