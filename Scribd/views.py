from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from rest_framework import generics, viewsets
from Scribd.user_model import User, UserManager
from Scribd.forms import EbookForm, RegisterForm, ProfileFormProvider
from Scribd.models import Ebook
from Scribd.serializers import UserSerializer, EbookSerializer

from django.http import HttpResponseRedirect
from django.urls import reverse


def provider_page(request):
    return render(request, 'scribd/providers_homepage.html')

def contract_page(request):
    return render(request, 'scribd/contract.html')

def support_page(request):
    return render(request, 'scribd/support_page.html')


class libro(object):

    def __init__(self, titulo, autor, descripcion, portada):
        self.titulo = titulo
        self.autor = autor
        self.descripcion = descripcion
        self.portada = portada


def base(request):

    return render(request, 'scribd/base.html')


"""
def lista_libros(request):
    l1 = libro("El señor de los anillos la comunidad del anillo", "John R.R. Tolkien", "Thriller", "/static/images/SACdA.jpg")
    l2 = libro("Harry potter y el prisionero de Azkaban", "Joanne Rowling", "Thriller", "/static/images/HP3.jpg")
    l3 = libro("Don quijote de la mancha", "Miguel de Cervantes Saavedra", "Thriller", "/static/images/Q.jpeg")

    libros = [l1, l2, l3]

    ctx = {"lista_libros": libros}

    return render(request, "scribd/mainpage.html", ctx)
"""


def ebook_create_view(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = EbookForm()
    return render(request, 'forms/add_book.html', {'book_form': form})

def edit_profile_page_provider(request):
    if request.method == "POST":
        form = ProfileFormProvider(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = ProfileFormProvider(instance=request.user)
    context = {
        "form": form
    }
    return render(request, 'forms/edit_provider_profile.html', context)


class ebookMainView(ListView):
    model = Ebook
    template_name = 'scribd/mainpage.html'


class ebookListView(ListView):
    model = Ebook
    template_name = 'scribd/ebooks_list.html'


class ebookDetailView(DetailView):
    model = Ebook
    template_name = 'scribd/ebook_detail.html'


class EbookViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all().order_by('id')
    serializer_class = EbookSerializer

    # permission_classes = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        return Ebook.objects.all().order_by('id')


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def add_books_form(request):
    return render(request, 'forms/add_book.html')


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_registration')
    serializer_class = UserSerializer

    # permission_classes = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        return User.objects.all().order_by('date_registration')


def login_create_view(request,backend='django.contrib.auth.backends.ModelBackend'):

    if request.method == "POST":
        login_form = AuthenticationForm(None, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user,backend)
            if user.user_type == "Provider":
                return redirect('provider_page')
            elif user.user_type == "support":
                return redirect('support_page')
            elif user.user_type == "admin":
                return HttpResponseRedirect(reverse('admin:index'))
            return redirect('mainpage')

    else:

        login_form = AuthenticationForm()

    return render(request, 'scribd/base.html', {'login_form': login_form})

def signup_create_view(request,backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':

        signup_form = RegisterForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = User.objects.create_user(
                email = signup_form.cleaned_data.get('email'),
                username=signup_form.cleaned_data.get('username'),
                first_name=signup_form.cleaned_data.get('first_name'),
                last_name=signup_form.cleaned_data.get('last_name'),
                password=signup_form.cleaned_data.get('password1'),
                card_titular = signup_form.cleaned_data.get('card_titular'),
                card_number=signup_form.cleaned_data.get('card_number'),
                card_expiration=signup_form.cleaned_data.get('card_expiration'),
                card_cvv=signup_form.cleaned_data.get('card_cvv'),
                subs_type=signup_form.cleaned_data.get('subs_type'))

            login(request, user,backend)
            if user.user_type == "provider":
                return redirect('provider_page')
            elif user.user_type == "support":
                return redirect('support_page')
            elif user.user_type == "admin":
                return HttpResponseRedirect(reverse('admin:index'))
            return redirect('mainpage')
    else:

        signup_form = RegisterForm()

    context = {
        "register_form" : signup_form
    }
    return render(request, 'registration/signup.html', context)



