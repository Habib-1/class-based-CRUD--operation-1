from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,UpdateView,DeleteView,ListView
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.

#class based views template view
class home(TemplateView):
    template_name='base.html'


#class based view ListView
class all_post(ListView):
    model=models.blog
    template_name='blog.html'
    context_object_name='post'

#Class Based Create Operation
class createPost(CreateView):
    model=models.blog 
    form_class = forms.blog_form
    template_name = 'blog_form.html'
    success_url = reverse_lazy('all_post')



#class based update operation
class edit_post(UpdateView):
    model=models.blog
    form_class=forms.blog_form
    template_name='blog_form.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('all_post')


#class Base Delete operation
class delete_post(DeleteView):
    model=models.blog
    template_name='delete.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('all_post')