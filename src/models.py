from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    
class tarea(models.Model):
    title = models.CharField(max_length=50)
    description =  models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
      
    def __str__(self):
        return self.title + '- by ' + self.user.username
    
class category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id'] 
        
class product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='src/', blank=True)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='Informacion del producto')
    price = models.FloatField()
    avaible = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name} -> {self.price}'
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
    