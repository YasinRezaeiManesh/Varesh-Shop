from django.db import models
from django.urls import reverse
from django_jalali.db import models as jalali_models
from account_module.models import User


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="عنوان")
    url_title = models.CharField(max_length=200, db_index=True, verbose_name="عنوان در url")
    is_active = models.BooleanField(verbose_name='فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductTags(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=200, db_index=True)
    url_title = models.CharField(verbose_name='عنوان در url', max_length=200, db_index=True)
    is_active = models.BooleanField(verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    tags = models.ForeignKey(ProductTags, verbose_name='تگ', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    is_active = models.BooleanField(verbose_name="فعال", default=False)
    is_delete = models.BooleanField(verbose_name="حذف شده")
    inventory = models.BooleanField(verbose_name='موجودی', default=False)
    image = models.ImageField(upload_to='images/products', blank=True, null=True, verbose_name='تصویر')
    slug = models.SlugField(max_length=200, default='', null=True, blank=True, unique=True, db_index=True,
                            verbose_name='عنوان در url')
    short_description = models.CharField(max_length=360, verbose_name='توضیحات کوتاه', null=True, db_index=True)
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products_detail', args=[self.slug])

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    parent = models.ForeignKey('ProductComment', on_delete=models.CASCADE, verbose_name='والد', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    shamsi_date = jalali_models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')
    text = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصول'
