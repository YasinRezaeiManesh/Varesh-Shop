from django.db import models

# Create your models here.


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ServiceTags(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    short_description = models.CharField(null=True, blank=True, max_length=200, verbose_name='توضیحات کوتاه')
    category = models.ManyToManyField('ServiceCategory', related_name='service_categories', verbose_name='دسته بندی')
    tags = models.ForeignKey(ServiceTags, verbose_name='تگ ها', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url', unique=True, db_index=True, default='')
    description = models.TextField(verbose_name="توضیحات")
    description2 = models.TextField(verbose_name="توضیحات دوم")
    image = models.ImageField(upload_to='images/service_image', verbose_name="تصویر")
    icon = models.ImageField(upload_to='images/service_image', verbose_name="آیکون", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'
