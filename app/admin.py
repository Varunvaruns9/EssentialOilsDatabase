from django.contrib import admin
from .models import Plant, EssentialOil, Through


admin.site.site_header = "Essential Oils Database"
admin.site.site_title = "Essential Oils Database"
admin.site.register(Plant)
admin.site.register(EssentialOil)
admin.site.register(Through)
