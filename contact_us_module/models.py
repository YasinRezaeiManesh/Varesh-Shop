from django.db import models
from django_jalali.db import models as jalali_models

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    message = models.TextField(verbose_name='پیام')
    response = models.TextField(verbose_name='پاسخ پیام', blank=True, null=True)
    shamsi_date = jalali_models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
