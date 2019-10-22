from django.contrib import admin
from .models import Metabolite, EssentialOil, Through


admin.site.site_header = "Essential Oils Database"
admin.site.site_title = "Essential Oils Database"
admin.site.register(Metabolite)
admin.site.register(EssentialOil)
admin.site.register(Through)
