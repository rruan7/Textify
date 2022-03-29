from django.contrib import admin
from .models import Textify

class TextifyAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

# Register your models here.

admin.site.register(Textify, TextifyAdmin)