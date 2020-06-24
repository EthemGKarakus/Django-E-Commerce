from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    parent=TreeForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    status = models.IntegerField(max_length=10,choices=STATUS)
    slug = models.SlugField(null=False,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by=["name"]

    def get_absolute_url(self):
        return reverse("category_detail",kwargs={"slug":self.slug})


class Product(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.IntegerField()
    minamount=models.IntegerField()
    image = models.ImageField(upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False,unique=True)
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe("<img src='{}' height=50 />".format(self.image.url))
    image_tag.short_description="Image"

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,upload_to="uploads/images")

    def __str__(self):
        return self.name
