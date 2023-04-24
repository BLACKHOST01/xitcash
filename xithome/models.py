from django.db import models

# Create your models here.


# class people(models.Models):
#     pass
    
class user(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    email = models.EmailField( default=False, max_length=254)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
class article(models.Model):
    body = models.TextField(max_length=1000)
    

    def __str__(self):
        return self.body

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'article'
        verbose_name_plural = 'articles'