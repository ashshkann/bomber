from django.contrib import admin
from .models import about_site, header_site, copy_right

# Register your models here.
admin.site.register(about_site)
admin.site.register(header_site)
admin.site.register(copy_right)