from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from Scribd import views
from Scribd.views import UserList, UserDetail
from Scribd.views import ebook_create_view, ebookListView, ebookDetailView, signup_create_view, login_create_view, \
    provider_page, ebookMainView, edit_profile_page_provider, contract_page

urlpatterns = [
    url(r'^$', ebookMainView.as_view(), name='mainpage'),
    url(r'^base/$', views.base, name='base'),
    url('ebooklist/', ebookListView.as_view(), name='ebook_custom_list'),
    url('ebookdetail/(?P<pk>[0-9]+)/$', ebookDetailView.as_view(), name='ebook_custom_detail'),
    url('addbook/', ebook_create_view, name='add_book'),
    url('provider/edit/$', edit_profile_page_provider, name='edituserprofileprovider'),
    url('contract/$', edit_profile_page_provider, name='edituserprofileprovider'),
    url('User/$', UserList.as_view()),
    url('User/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url('accounts/login/', login_create_view, name='login'),
    url('accounts/signup/', signup_create_view, name='signup'),
    url('provider/', provider_page, name='provider_page'),
    url('contract/', contract_page, name='contract_page'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += staticfiles_urlpatterns()
