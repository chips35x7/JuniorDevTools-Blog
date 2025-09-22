from django.views.generic import ListView, View, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import Blog, Category, Comment
from .forms import BlogForm, CommentForm

USER_MODEL = get_user_model()


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/list.html'
    context_object_name = 'blog_list'


class CommentGet(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form': CommentForm})
        return context


class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    form_class = CommentForm
    template_name = 'blogs/detail.html'

    def get_object(self, queryset = None):
        obj = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.blog = self.get_object()
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        blog = self.get_object()
        return reverse('blog_detail', kwargs={'pk': blog.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blogs/comment_delete.html'
    
    def get_success_url(self):
        blog = get_object_or_404(Blog, pk=self.get_object().blog_id)
        return reverse('blog_detail', kwargs={'pk': blog.pk})
    
    def test_func(self):
        return self.request.user.pk == self.get_object().user_id


class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)        


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'blogs/create.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        blog_form = form.save(commit=False)
        blog_form.author = self.request.user
        blog_form.save()
        return super().form_valid(form)
    
class BlogCategoryListView(ListView):
    model = Category
    template_name = 'blogs/categories.html'
    context_object_name = 'categories'


class BlogCategoryDetailView(DetailView):
    model = Category
    template_name = 'blogs/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        blogs = get_list_or_404(Blog, category_id = self.get_object().id)
        context = super().get_context_data(**kwargs)
        context.update({'blogs': blogs})
        return context
    

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/update.html'

    def get_success_url(self):
        blog = self.get_object()
        return reverse('blog_detail', kwargs={'pk': blog.pk})
    
    def test_func(self):
        user = self.get_object().author
        return self.request.user.pk == user.pk
    

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/delete.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        user = self.get_object().author
        return self.request.user.pk == user.pk
    

class MyBlogsView(LoginRequiredMixin, DetailView):
    template_name = 'blogs/my_blogs.html'
    
    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj
    
    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context.update({
            'my_blogs': user.blog_set.all
        })
        return context
    

class SearchResultsListView(ListView):
    model = Blog
    template_name = 'blogs/search_results.html'
    context_object_name = 'blog_list'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Blog.objects.filter(
            Q(topic__icontains=query) | Q(body__icontains=query)
        )