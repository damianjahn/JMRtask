from django.contrib import admin

# Register your models here.
from urlshortener.models import Urlshortcut

admin.site.register(Urlshortcut)
