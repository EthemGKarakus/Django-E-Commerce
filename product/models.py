from django.db import models

# Create your models here.
class Category(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    parent=models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    status = models.IntegerField(max_length=10,choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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
    detail = models.TextField(blank=True)
    slug = models.SlugField()
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name