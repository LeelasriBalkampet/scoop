# news/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def article_list(request):
    # You would typically fetch articles from your database here
    return render(request, 'article_list.html')

def article_detail(request, id):
    # Fetch the article by id from your database
    return render(request, 'article_detail.html')

def event_list(request):
    # You would typically fetch events from your database here
    return render(request, 'event_list.html')

def event_detail(request, id):
    # Fetch the event by id from your database
    return render(request, 'event_detail.html')

def submission_form(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'submission_form.html')

def admin_dashboard(request):
    # Fetch pending submissions for review
    return render(request, 'admin_dashboard.html')

def category_list(request):
    # Fetch all categories
    return render(request, 'category_list.html')

def category_articles(request, category):
    # Fetch articles/events filtered by category
    return render(request, 'category_articles.html', {'category': category})
