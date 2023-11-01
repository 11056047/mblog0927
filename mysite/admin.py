from django.contrib import admin
from mysite.models import Post,Product
# Register your models here.

class PostAdaim(admin.ModelAdmin):
    list_display=("title",'slug','pub_date')


admin.site.register(Post,PostAdaim)
admin.site.register(Product)

