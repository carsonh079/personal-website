from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Project(models.Model):
    PROJECT_TYPES = [
        ('data_analysis', 'Data Analysis'),
        ('data_engineering', 'Data Engineering'),
        ('web_dev', 'Web Development'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='other')
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
