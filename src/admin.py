from django.contrib import admin
from .models import Programmer, tarea, category, product

class tareaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.

admin.site.register(Programmer)
admin.site.register(tarea, tareaAdmin)
admin.site.register(category)
admin.site.register(product)
