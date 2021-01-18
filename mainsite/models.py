from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)  # 文章標題
    slug = models.CharField(max_length=200)  # 文章網址
    body = models.TextField()  # 文章內容
    pub_date = models.DateTimeField(default=timezone.now)  # 發文時間

    class Meta:  # 文章顯示的順序
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
