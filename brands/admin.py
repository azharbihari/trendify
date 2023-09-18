from django.contrib import admin
from brands.models import Brand


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand)
