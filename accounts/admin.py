from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Profile", {"fields": [
        "date_of_birth", "bio", "avatar", "sex"]}),)


admin.site.register(Account, AccountAdmin)


# Customize the default admin site attributes
admin.site.site_header = 'Trendify Administration'
admin.site.index_title = 'Welcome to Trendify Administration'
