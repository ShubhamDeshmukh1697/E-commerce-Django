from django.contrib import admin
from .models import Product,Contact,Orders,OrderUpdate

# Register your models here.
@admin.register(Product)
class shopAdmin(admin.ModelAdmin):
    list_display=['product_name','category','price','desc','pub_date']

@admin.register(Contact)
class shopAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','desc']

admin.site.register(Orders)
admin.site.register(OrderUpdate)
