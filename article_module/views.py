from django.shortcuts import render
from django.views.generic import ListView, DetailView
from utils.convertors import group_list
from article_module.models import Article, ArticleGallery, ArticleComment, ArticleCategory


# Create your views here.


class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        return query


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_module/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        galleries = list(ArticleGallery.objects.filter(article_id=article.id).all())
        context['galleries'] = galleries
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent=None, success=True)
        return context


def article_category_component(request):
    context = {
        'main_categories': ArticleCategory.objects.filter(is_active=True),
    }
    return render(request, 'article_module/components/article_category_component.html', context)


def add_article_comment(request):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('articleComment')
        parent_id = request.GET.get('parent_id')
        new_comment = ArticleComment(article_id=article_id, text=article_comment, parent_id=parent_id, user_id=request.user.id)
        new_comment.save()

        context = {
            'comments': ArticleComment.objects.filter(article_id=article_id, parent=None).order_by('shmasi_time').prefetch_related('articlecomment_set')
        }

        return render(request, 'article_module/include/article_comment_partial.html', context)
