from django.urls import path
from wiki.views import ArticleListView, ArticleDetailView, ArticleCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ArticleListView.as_view(), name='wiki-list-page'),
    path('w/<str:slug>/', ArticleDetailView.as_view(), name='wiki-details-page'),
    path('/new_article/', ArticleCreateView.as_view(), name='wiki-create-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
