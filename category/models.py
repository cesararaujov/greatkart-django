from django.db import models
from django.urls import reverse

# Create your models here.
class Cateogory(models.Model):

    Cateogory_name = models.CharField(max_length=50, unique=True,default="")
    slug = models.SlugField(max_length=100, unique=True,default="")
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    class Meta:
        verbose_name='category'
        verbose_name_plural ='categories'

    def __str__(self):
        return self.Cateogory_name
