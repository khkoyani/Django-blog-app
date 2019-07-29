from django.shortcuts import render, get_object_or_404
from .models import Post2
# imports the post model so it can be used to query db and pass to context for render to html
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    context = {'posts': Post2.objects.all(), 'title': 'blog_home'}
    # Post2.objects.all()querys the database and passes a queryset so it can be run in the for loop
    return render(request, 'blog/home.html', context)


def about(request):
    context = {'title': 'blog_about'}
    return render(request, 'blog/about.html', context)


class PostListView(ListView):
    model = Post2
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5


class AuthorPostListView(ListView):
    model = Post2
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date']     moved to the getqueryset method since it's being overwritten
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post2.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = Post2
    # template_name = default will be   <appname/modelname_viewtype   in this case. blog/post2_detail


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post2
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post2
    fields = ['title', 'content']

    def form_valid(self, form):  # sends the form that was submitted to the the function
        form.instance.author = self.request.user  # the form only has title and content so need to define author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        # def test_func(self, form):
        # if self.request.user == form.instance.author.   Tried to do this but it doesnt work because this function is run at the
        # very beginning and the form has not been init yet. more on onenote


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    model = Post2
    success_url = '/'
