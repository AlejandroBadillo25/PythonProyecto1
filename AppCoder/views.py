from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        post_list = Post.objects.filter(title__icontains=busqueda)
    else: 
        post_list = Post.objects.all()
    return render(request, 'AppCoder/post_list.html', context={"posts": post_list})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('AppCoder:post_list')
        else:
            form.add_error(None, "Debes estar logeado para poder publicar")
    else: 
        form = PostForm()
    return render(request, 'AppCoder/post_create.html', context={"form": form}) 