from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from blog.models import Post,Comment
from django.shortcuts import get_object_or_404,redirect
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# from django.urls import redirect
# Create your views here.

# class welcome(CreateView):
#     template_name ='blog/base.html'

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ('author','title','text')
    template_name = 'blog/post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(ListView):
    model = Post
    template_name = 'blog/draft_list.html'


def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
        else:
            print(comment.errors)
    else:
        comment = CommentForm()
    return render(request,'blog/add_comment.html',context={'form':comment})

@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def delete_comment(request, pk):
    comment =get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
