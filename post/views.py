from dataclasses import field
from re import template
from time import strftime
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Post
    # queryset = Post.objects.filter(date_posted=datetime.now())
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    extra_context = {'datetime': datetime.now(), 'name': 'Nurs'}
    ordering = '-date_posted'
    paginate_by = 2
    page_kwarg = 'stranica'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['age'] = 28
        return context

    def get_queryset(self):
        question = self.request.GET.get('q')
        if question:
            return self.model.objects.filter(title__icontains=question)
        else:
            return self.model.objects.all()

class SearchView(TemplateView):
    template_name = 'seatch_field.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'id'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        return context

    def get_queryset(self):
        return self.model.objects.filter(date_posted=datetime.now())


class PostCreateView(CreateView):
    form_class = PostForm
    # model = Post
    # fields = '__all__'
    template_name = 'post_form.html'
    initial = {'title': 'Заголовок'}
    prefix = 'my'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date_posted = datetime.now()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post

    def delete(self):
        return super().delete()



def test_list_view(request):
    queryset = Post.objects.all()
    print(str(queryset.query))
    for i in queryset:
        print(i)
    return render(request, 'test.html', {'queryset': queryset})