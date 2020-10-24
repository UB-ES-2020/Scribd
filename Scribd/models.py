from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator
# Create your models here.

class Ebook(models.Model):
    TYPE_FILE = (
        ("pdf", "pdf"),
        ("epub", "epub"),
    )
    _type_files = dict(TYPE_FILE)
    ebook_number = models.CharField(max_length=8, unique=True,default='')
    title = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    description = models.TextField(default='')
    is_promot = models.BooleanField(default='False')
    size = models.IntegerField()
    media_type= models.CharField(max_length=5, choices=TYPE_FILE)
    featured_photo = models.ImageField(upload_to="scribd/static/images/",default='scribd/static/images/')
    count_downloads = models.PositiveIntegerField()


    def get_ebook_media_type(self):
        return self._type_files[self.media_type]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ebook'
        verbose_name_plural = 'Ebooks'


class ViewedEbook(models.Model):
    id_vr = models.AutoField(primary_key=True)
    ebook = models.ManyToManyField(Ebook, through='EbookInsertDate')


class EbookInsertDate(models.Model):
    viewed_ebooks = models.ForeignKey(ViewedEbook, on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Review(models.Model):
    STARS = (
        ("One star", 1),
        ("Two stars", 2),
        ("Three stars", 3),
        ("Four stars", 4),
        ("Five stars", 5),
    )
    _d_stars = dict(STARS)
    id = models.AutoField(primary_key=True)
    ebook = models.ForeignKey(Ebook,on_delete=models.CASCADE)
    value_stars = models.CharField(max_length=12, choices=STARS)
    comment = models.TextField()
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    def get_human_stars(self):
        return self._d_stars[self.value_stars]