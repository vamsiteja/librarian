from django.db import models
from datetime import datetime


class Issue(models.Model):
    student_id = models.CharField(max_length=6)
    student_name = models.CharField(max_length=50)
    book_id = models.CharField(max_length=30)
    book_name = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.student_id+ ' - ' + self.book_id