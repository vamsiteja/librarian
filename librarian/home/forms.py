from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['student_id', 'student_name', 'book_id', 'book_name']


class RenewalForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['student_id', 'book_id']