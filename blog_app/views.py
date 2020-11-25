from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from blog_app.models import Post, Sub_Category, Main_Category, Comment
from django.db.models import Q


def get_query_obj(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Post.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))

def Blog(request):
    query = ""
    post = Comment.objects.all()
    t_comments = post.total_comments
    posts = get_query_obj(query)
    main_category = Main_Category.objects.all()
    sub_category = Sub_Category.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts, 'sub_category': sub_category, 'total_comments': t_comments,
        'main_category': main_category, 'page_obj': page_obj
    }
    if request.GET:
        query = request.GET.get('q')
        context['query'] = str(query)
    return render(request, "blog.html", context)


def detail(request, pk):
    posts = Post.objects.all()
    main_category = Main_Category.objects.all()
    sub_category = Sub_Category.objects.all()
    post = Post.objects.get(pk=pk)
    t_comments = post.comments.count()
    context = {
        'post': post, 'posts': posts, 'main_category': main_category, 'sub_category': sub_category,
        'total_comments': t_comments
    }
    return render(request, "single-blog.html", context )


def save_comment(request):
    if request.method != "POST":
        return HttpResponse("<h1> Invalid Method </h1>")
    else:
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        post = request.POST.get("post_id")
        try:
            comment = Comment(body=message, emaill=email, full_name=full_name)
            comment.post_id = post
            comment.save()
            return HttpResponseRedirect("/detail/"+{{ post }})
        except:
           return HttpResponseRedirect("/detail/"+{{ post }})


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        send_mail(name, subject, email, message, ['contact@optimize.com'])
        return render(request, "contact.html")
    else:
        return render(request, "contact.html")


def category(request, category_name):
    posts = Post.objects.all()
    categories = Post.objects.filter(main_category=category_name)
    sub_category = Sub_Category.objects.all()
    paginator = Paginator(categories, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'categories': categories, 'posts': posts, 'page_obj': page_obj, 'sub_category': sub_category}
    return render(request, "main_category.html", context)

