from django.contrib import admin

from .models import Ebook, ViewedEbooks, Review, EbookInsertDate, UserTickets
# Register your models here
from .refactor_models import User, providerProfile, supportProfile, userProfile


class EbookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User)
admin.site.register(providerProfile)
admin.site.register(supportProfile)
admin.site.register(userProfile)

admin.site.register(Ebook)
admin.site.register(Review)
admin.site.register(ViewedEbooks)
admin.site.register(EbookInsertDate)
admin.site.register(UserTickets)
# Configurar el titulo del panel admin
title = "Administration Scribd"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Management Panel"
