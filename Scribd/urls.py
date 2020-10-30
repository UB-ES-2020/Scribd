from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from Scribd import views
from Scribd.views import UserList, UserDetail
from Scribd.views import lista_libros, base, ebookList, ebookDetail, ebook_create_view, ebookListView, \
    ebookDetailView, signup_create_view, login_create_view

# endpoints

urlpatterns = [
    url(r'^$', views.lista_libros, name='mainpage'),
    url(r'^base/$', views.base, name='base'),
    url('ebook/$', ebookList.as_view()),
    url('ebook/(?P<pk>[0-9]+)/$', ebookDetail.as_view()),
    url('User/$', UserList.as_view()),
    url('User/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url('addbook/', ebook_create_view, name='add_book'),
    url('accounts/login/', login_create_view, name='login'),
    url('accounts/signup/', signup_create_view, name='signup'),
    url('User/$', UserList.as_view()),
    url('User/(?P<pk>[0-9]+)/$', UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
