from django.urls import path
from blog_app.views import detail, Blog, save_comment, contact, category

urlpatterns = [
    path('', Blog, name="blog"),
    path('detail/<int:pk>/', detail, name="detail"),
    path('save_comment', save_comment),
    path('contact', contact, name="contact"),
    path('category/<str:category_name>', category, name="category")
]