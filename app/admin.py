# your_app_name/admin.py
from django.contrib import admin
from .models import ExtractedText

admin.site.register(ExtractedText)