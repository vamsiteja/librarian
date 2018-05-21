from django.conf.urls import url
from . import views
from django.contrib import  admin
app_name = 'home'
urlpatterns = [
    url(r'admin',admin.site.urls),
    url(r'issues', views.issues, name='issues'),
    url(r'login', views.log, name='login'),
    url(r'logout', views.log_out, name='logout'),
    url(r'returns', views.returns, name='returns'),
    url(r'renewals', views.renewals, name='renewals'),
    url(r'issue_send', views.issue_send, name='issue_send'),
    url(r'renewal_send', views.renewal_send, name='renewal_send'),
    url(r'return_send', views.return_send, name='return_send'),
    url(r'getbooks', views.getbooks, name='getbooks'),
    url(r'^$', views.home, name='home'),
]