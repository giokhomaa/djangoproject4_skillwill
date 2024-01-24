from django.urls import path
from .views import (BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
                    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView)


urlpatterns = [
    path('book/<int:pk>/', BookListView.as_view, name='book_detail'),
    path('book/list/', BookDetailView.as_view, name='book_list'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view, name='book_edit'),
    path('book/new/', BookCreateView.as_view, name='book_create'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view, name='book_delete'),
    # path('author/<int:pk>/', views.author_detail, name='author_detail'),
    # path('author/<int:pk>/edit/', views.author_edit, name='author_edit'),
    # path('author/list/', views.author_list, name='author_list'),
    # path('author/new/', views.author_new, name='author_new')
    path('author/<int:pk>/', AuthorListView.as_view, name='author_detail'),
    path('author/list/', AuthorDetailView.as_view, name='author_list'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view, name='author_edit'),
    path('author/new/', AuthorCreateView.as_view, name='author_create'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view, name='author_delete')
]