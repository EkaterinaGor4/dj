from django.contrib import admin

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'lte_exists', 'slug']
    list_filter = ['name', 'price']