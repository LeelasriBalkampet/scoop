# news/admin.py

from django.contrib import admin
from .models import Article, Event, Category, Submission

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    search_fields = ('title', 'content')
    list_filter = ('category', 'pub_date')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'category')
    search_fields = ('name', 'description', 'location')
    list_filter = ('category', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'submission_date', 'approved')
    search_fields = ('title', 'content')
    list_filter = ('category', 'approved')
    actions = ['approve_submissions']

    def approve_submissions(self, request, queryset):
        queryset.update(approved=True)
    approve_submissions.short_description = "Approve selected submissions"