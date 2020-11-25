from django.db import models

class Main_Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    info = models.TextField()

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField()
    title = models.CharField(max_length=250)
    likes = models.IntegerField(default=0, null=True, blank=True)
    description = models.TextField()
    main_category = models.ForeignKey(Main_Category, related_name="main_category", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, related_name="sub_category", on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()



class Comment(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    body = models.TextField()
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def total_comments(self):
        return self.post_id.count()
