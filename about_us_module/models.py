from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title_1 = models.CharField(max_length=100, verbose_name='عنوان اول')
    image_1 = models.ImageField(upload_to='images/about_us', verbose_name='تصویر اول')
    description_1 = models.TextField(verbose_name='توضیحات اول')
    title_2 = models.CharField(max_length=100, verbose_name='عنوان دوم')
    image_2 = models.ImageField(upload_to='images/about_us', verbose_name='تصویر دوم')
    description_2 = models.TextField(verbose_name='توضیحات دوم')
    home_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان صفحه خانه')
    home_image = models.ImageField(upload_to='images/about_us', null=True, blank=True, verbose_name='تصویر صفحه خانه')
    home_description = models.TextField(null=True, blank=True, verbose_name='توضیحات صفحه خانه')
    tag_1 = models.CharField(verbose_name='تگ 1', null=True, blank=True, max_length=100)
    tag_2 = models.CharField(verbose_name='تگ 2', null=True, blank=True, max_length=100)
    tag_3 = models.CharField(verbose_name='تگ 3', null=True, blank=True, max_length=100)
    tag_4 = models.CharField(verbose_name='تگ 4', null=True, blank=True, max_length=100)
    tag_5 = models.CharField(verbose_name='تگ 5', null=True, blank=True, max_length=100)

    def __str__(self):
        return f'{self.title_1} - {self.title_2}'

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
