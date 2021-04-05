from django.contrib.auth.models import User
from django.db import models

# from django.template.defaultfilters import slugify
from uuslug import uuslug


class Product(models.Model):
    # поля, которые вводит пользователь в форме
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, blank=True, null=True
    )
    link = models.URLField(max_length=200, default="http://localhost")
    is_granted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    #   далее поля, которые берутся не из формы
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Product, self).save(*args, **kwargs)
