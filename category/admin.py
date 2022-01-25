from django.contrib import admin
from .models import Cateogory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Cateogory_name','slug')
    prepopulated_fields = {'slug': ('Cateogory_name',)}



admin.site.register(Cateogory,CategoryAdmin)
