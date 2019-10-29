from django.contrib import admin
from .models import Metabolite, EssentialOil, Through


# Parameters for admin site
admin.site.site_header = "Essential Oils Database"
admin.site.site_title = "Essential Oils Database"
admin.site.index_template = "admin_index.html"
admin.site.index_title = ""
admin.site.register(Metabolite)
admin.site.register(EssentialOil)
admin.site.register(Through)
