from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Project


def home(request):
    """Landing page with links to resume, blog, and projects"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_posts = BlogPost.objects.filter(published=True)[:3]

    context = {
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
    }
    return render(request, 'portfolio/home.html', context)


def blog_list(request):
    """List of all published blog posts"""
    posts = BlogPost.objects.filter(published=True)
    context = {'posts': posts}
    return render(request, 'portfolio/blog_list.html', context)


def blog_detail(request, slug):
    """Individual blog post"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    context = {'post': post}
    return render(request, 'portfolio/blog_detail.html', context)


def project_list(request):
    """List of all projects"""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/project_list.html', context)


def project_detail(request, slug):
    """Individual project"""
    project = get_object_or_404(Project, slug=slug)
    context = {'project': project}
    return render(request, 'portfolio/project_detail.html', context)
