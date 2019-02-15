from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from . import models

class ArticleListView(ListView):
	model = models.Article 
	template_name = 'article_list.html'
	login_url = 'login'
class ArticleDetailView(DetailView): 
	model = models.Article
	template_name = 'article_detail.html'
	login_url = 'login'

class ArticleCreateView(LoginRequiredMixin, CreateView): 
	model = models.Article
	template_name = 'article_new.html' 
	fields = ['title', 'body',]
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ArticleUpdateView(UpdateView): 
	model = models.Article
	fields = ['title', 'body', ] 
	template_name = 'article_edit.html'
	login_url = 'login'

class ArticleDeleteView(DeleteView): 
	model = models.Article
	template_name = 'article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'
	
# Create your views here.
