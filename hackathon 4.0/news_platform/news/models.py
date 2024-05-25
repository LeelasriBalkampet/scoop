# news/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Submission(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def _str_(self):
        return self.title