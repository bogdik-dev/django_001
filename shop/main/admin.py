from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}#Эти поля заполняй автоматически на основе других полей "slug" — какое поле заполнять автоматически. Это ключ словаря
                                                                                                      #("name",) — на основе какого поля (или полей). Это кортеж (обрати внимание на запятую после name — она обязательна
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "status", "created", "updated"]#список колонок, которые Django покажет в таблице списка товаров в админке
    list_filter = ["status", "created", "updated", "category"]#только поля с «вариантами»
    list_editable = ["price", "status"]#колонки, которые можно редактировать прямо в списке товаров, не открывая каждый по отдельности
    prepopulated_fields = {"slug": ["name"]}
    #python manage.py createsuperuser
    #python manage.py runserver