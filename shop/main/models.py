from django.conf import settings #дай мне доступ к настройкам проекта прямо из кода модели. Это нужно для author = models.ForeignKey(settings.AUTH_USER_MODEL,...)
from django.db import models#возьми из библиотеки Django модуль db (то есть базу данных), а из него — класс models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)#models. - я не обращаюсь к своему файлу,а беру из инструментария Django тип поля "текстовое поле" и даю его полю name
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):#****
        return reverse('main:product_list_by_category', args=[self.slug])#***

class Product(models.Model):
    class StockStatus(models.TextChoices):#описать список разрешённых значений для поля «в наличии» / «нет в наличии
        IN_STOCK = "in_stock", "В наличии"              #слева - то, что ляжет в базу
        OUT_OF_STOCK = "out_of_stock", "Нет в наличии"  #справа - то, что увидит тип в админке
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100, db_index=True) #имя товара
    slug = models.SlugField(max_length=100, unique=True)    #ссылка на товар
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)#это шаблон пути для хранения загружаемых файлов (картинок товаров)
    #MEDIA_ROOT — локальная папка на сервере или твоём компьютере где все загруженные пользователями файлы
    description = models.TextField(blank=True)#типа для описания?
    price = models.DecimalField(max_digits=10, decimal_places=2)#денежки
    status = models.CharField(max_length=15, choices=StockStatus.choices, default=StockStatus.IN_STOCK)#возьми из этого класса уже подготовленный список, поэтому и пишем .choices
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):#****
            return reverse('main:product_detail', args=[self.id, self.slug])


























'''
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        # В видео была ошибка: без запятой это не кортеж, Django выдаст ошибку.
        # Правильно: ('name',) или просто 'name' (как в новой версии Django)
        ordering = ('name',) 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Как в видео: ссылка на фильтрацию по категории
        return reverse('main:product_list_by_category', args=[self.slug])


class Product(models.Model):
    # Здесь я исправил опечатку: Category, вместо Category; и prodycts на products
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Как в видео: ссылка на детальную страницу товара
        return reverse('main:product_detail', args=[self.id, self.slug])
'''