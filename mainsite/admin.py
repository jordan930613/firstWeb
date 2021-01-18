from django.contrib import admin
# 引入Post類別
from .models import Post

# Register your models here.

# 自訂Post顯示的方式


class PostAdmin(admin.ModelAdmin):
    # 顯示title,slug,pub_date
    list_display = ('title', 'slug', 'pub_date')


# 透過register註冊
admin.site.register(Post, PostAdmin)
