from django.shortcuts import render
from .forms import IssueForm, RenewalForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from .models import Issue
from django.db.models import Q
# Create your views here.



def home(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/home.html');


def issues(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        data = {
            'today_date': datetime.now(),
        }
        return render(request, 'home/issues.html', data);


def returns(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        data = {
            'today_date': datetime.now(),
        }
        return render(request, 'home/returns.html', data);


def renewals(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        data = {
            'today_date': datetime.now(),
        }
        return render(request, 'home/renewals.html', data)


def issue_send(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        form = IssueForm(request.POST or None)
        if form.is_valid():
            obj = Issue.objects.filter(
                Q(book_id=form.cleaned_data.get('book_id')), Q(student_id=form.cleaned_data.get('student_id')))
            if obj:
                return render(request, 'home/issues.html', {
                    'issue_fail': 'The issual is done Already', 'today_date': datetime.now()})
            issue_object = form.save(commit=False)
            issue_object.save()
            return render(request, 'home/home.html', {
                'issue_success': 'yes',
                'book_name': form.cleaned_data.get('book_name'),
                'student_name': form.cleaned_data.get('student_name'),
            })
        else:
            return render(request, 'home/issues.html', {
                'issue_fail': 'The Form is not Valid', 'today_date': datetime.now()})


def renewal_send(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        form = RenewalForm(request.POST or None)
        if form.is_valid():
            renewal_object = Issue.objects.filter(
                Q(book_id=form.cleaned_data.get('book_id')), Q(student_id=form.cleaned_data.get('student_id')))
            if renewal_object:
                renewal_object.issue_date = datetime.now()
                return render(request, 'home/home.html', {
                    'renewal_success': 'yes',
                    'book_name': renewal_object[0].book_name,
                    'student_name': renewal_object[0].student_name,
                })
            else:
                return render(request, 'home/renewals.html', {
                    'renewal_fail': 'No book issued to that name', 'today_date': datetime.now()})
        else:
            return render(request, 'home/renewals.html', {
                'renewal_fail': 'The Form is not Valid', 'today_date': datetime.now()})


def return_send(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        form = RenewalForm(request.POST or None)
        if form.is_valid():
            return_object = Issue.objects.filter(
                Q(book_id=form.cleaned_data.get('book_id')), Q(student_id=form.cleaned_data.get('student_id')))
            if return_object:
                data = {
                    'return_success': 'yes',
                    'book_name': return_object[0].book_name,
                    'student_name': return_object[0].student_name,
                }
                return_object.delete()
                return render(request, 'home/home.html', data)
            else:
                return render(request, 'home/returns.html', {
                    'return_fail': 'No book issued to that name', 'today_date': datetime.now()})
        else:
            return render(request, 'home/returns.html', {
                'return_fail': 'The Form is not Valid', 'today_date': datetime.now()})


def log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/home.html', {'login_success': 'You Have Logged in succesfully!!!'})
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'home/login.html')


def log_out(request):
    logout(request)
    return render(request, 'home/login.html', {'error_message': 'Successfully Logged out'})


def getbooks(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        books = Issue.objects.filter(student_id=student_id)
        return render(request, 'home/home.html', {
            'books': books, 'number': Issue.objects.filter(student_id=student_id).count()})
