from django.contrib import admin

from .models import Category, Checklist, User

# Register your models here.

admin.site.register(Category)
admin.site.register(Checklist)
admin.site.register(User)
