from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):  #/admin에서 Blogs object대신 글제목이 나오게함
        return self.title

    def summary(self):
        return self.body[:100]