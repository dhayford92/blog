from django.contrib import admin
from blog_app.models import Post, Main_Category, Sub_Category, Comment



admin.site.register(Post)
admin.site.register(Main_Category)
admin.site.register(Sub_Category)
admin.site.register(Comment)