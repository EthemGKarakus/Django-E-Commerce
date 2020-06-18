from django.contrib import admin


from product.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent','status']
    list_filter = ['parent', 'status']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','status']
    list_filter = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)