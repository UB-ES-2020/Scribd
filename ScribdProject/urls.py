"""ScribdProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from rest_framework import routers

from Scribd.views import (
    EbookViewSet,
    AccountsViewSet,
    ticketViewSet,
    UploadsViewSet,
    ForumViewSet,
    error404,
    error500,
)

router = routers.DefaultRouter()
router.register(r"ebooks", EbookViewSet)
router.register(r"accounts", AccountsViewSet)
router.register(r"uploaded_files", UploadsViewSet)
router.register(r"tickets", ticketViewSet)
router.register(r"forums", ForumViewSet)

urlpatterns = [
    url(r"admin/", admin.site.urls, name="admin_page"),
    url(r"", include("Scribd.urls")),
    url(r"", include("Scribd.urls")),
    url(r"api/", include(router.urls)),
    url(r"api-auth/", include("rest_framework.urls",
                              namespace="rest_framework")),
    url(r"^oauth/", include("social_django.urls", namespace="social")),
    url("accounts/", include("django.contrib.auth.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error404
handler500 = error500
