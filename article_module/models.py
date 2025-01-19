from django.db import models
from django_jalali.db import models as jalali_models
from account_module.models import User


# Create your models here.


class ArticleCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ArticleTags(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان", db_index=True)
    url_title = models.CharField(max_length=200, verbose_name="عنوان در url", db_index=True)
    is_active = models.BooleanField(verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    category = models.ManyToManyField(ArticleCategory, related_name='article_categories', verbose_name='دسته بندی ها')
    tags = models.ForeignKey(ArticleTags, on_delete=models.CASCADE, verbose_name='تگ', null=True, blank=True)
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    description2 = models.TextField(verbose_name='توضیحات 2', blank=True, null=True)
    slug = models.SlugField(max_length=200, default='', null=True, blank=True, unique=True, db_index=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')
    shamsi_date = jalali_models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    image = models.ImageField(upload_to='images/article_gallery', verbose_name='تصویر')

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    shmasi_time = jalali_models.jDateTimeField(auto_now_add=True, verbose_name='زمان شمسی')
    shmasi_date = jalali_models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')
    text = models.TextField(verbose_name='متن کامنت')
    success = models.BooleanField(default=False, verbose_name="تایید شده")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'
