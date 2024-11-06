from django.db import models

# Create your models here.


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    phone = models.IntegerField(verbose_name='شماره تماس')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='آدرس ایمیل')
    instagram = models.CharField(max_length=100, null=True, blank=True, verbose_name='صفحه اینستاگرام')
    telegram = models.CharField(max_length=100, null=True, blank=True, verbose_name='آیدی تلگرام')
    whatsapp = models.IntegerField(null=True, blank=True, verbose_name='شماره واتساپ')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    time_working = models.TextField(max_length=100, verbose_name='ساعات کاری')
    short_description = models.TextField(verbose_name='توضیحات کوتاه', default='')
    logo = models.ImageField(null=True, blank=True, upload_to='images/logo', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'

    def __str__(self):
        return self.site_name


class SiteQuestions(models.Model):
    question = models.CharField(max_length=200, verbose_name='سوال')
    answer = models.TextField(verbose_name='پاسخ')
    url_title = models.CharField(verbose_name='', unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'سوالات'
        verbose_name_plural = 'سوالات'


class SiteCertificate(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/Certificate', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گواهینامه'
        verbose_name_plural = 'گواهینامه ها'


class SiteTeam(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    image = models.ImageField(upload_to='images/team_profile', verbose_name='تصویر پروفایل')
    job = models.CharField(max_length=200, verbose_name='شغل')
    instagram = models.CharField(max_length=200, verbose_name='آیدی اینستاگرام', null=True, blank=True)
    twitter = models.CharField(max_length=200, verbose_name='آیدی توییتر', null=True, blank=True)
    telegram_app = models.CharField(max_length=200, verbose_name='آیدی تلگرام', null=True, blank=True)
    whatsapp = models.CharField(max_length=200, verbose_name='شماره واتساپ', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اعضائ تیم'
        verbose_name_plural = 'اعضائ تیم'
