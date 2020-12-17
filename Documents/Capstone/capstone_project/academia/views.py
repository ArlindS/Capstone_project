from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import (
    Post,
    ResourceCS,
    ResourceTh,
    ResourceDs,
    ResourceCe,
    ResourceAlg,
    ResourceAlg_Graphs,
    ResourceGraphs
)
from django.shortcuts import render
# .models = in current directory


def home(request):
    return render(request, 'academia/home.html')


def compSci(request):
    context = {'resource': ResourceCS.objects.all()}
    return render(request, 'academia/compSci.html', context)


def theoretical(request):
    context = {'resource': ResourceTh.objects.all()}
    return render(request, 'academia/theoretical.html', context)


def dataSci(request):
    context = {'resource': ResourceDs.objects.all()}
    return render(request, 'academia/dataSci.html', context)


def compEng(request):
    context = {'resource': ResourceCe.objects.all()}
    return render(request, 'academia/compEng.html', context)


def about(request):
    return render(request, 'academia/about.html', {'title': 'About'})


def discussion_CS(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'academia/discussion_CS.html', context)


def algorithms(request):
    context = {'resource': ResourceAlg.objects.all()}
    return render(request, 'academia/algorithms.html', context)


def algo_graph(request):
    context = {'resource': ResourceAlg_Graphs.objects.all()}
    return render(request, 'academia/algo_graph.html', context)


def graph(request):
    context = {'resource': ResourceGraphs.objects.all()}
    return render(request, 'academia/graph.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'academia/discussion_CS.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'academia/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'acedemia/about.html', {'title': 'About'})
