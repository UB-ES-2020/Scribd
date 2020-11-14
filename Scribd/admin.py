from django.contrib import admin

from .models import Ebook, ViewedEbooks, Review, EbookInsertDate, User
# Register your models here
from .user_model import SubscribedUsers


class EbookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Ebook)
admin.site.register(Review)
admin.site.register(ViewedEbooks)
admin.site.register(EbookInsertDate)
admin.site.register(User)
admin.site.register(SubscribedUsers)

# Configurar el titulo del panel admin
title = "Administration Scribd"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Management Panel"
