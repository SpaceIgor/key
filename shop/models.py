from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import DecimalValidator
from .validators import validate_non_negative_price, validate_category_nesting_level


class Category(MPTTModel):
    name = models.CharField('Назва', max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            validators=[validate_category_nesting_level])

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Назва', max_length=255)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2,
                                validators=[DecimalValidator(10, 2),
                                            validate_non_negative_price])
    categories = models.ManyToManyField(Category, verbose_name='Категорії')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

    def __str__(self):
        return self.name

