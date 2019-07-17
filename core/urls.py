from django.urls import path

from core.views import (
    AuthorDetailView, AuthorListView, ChangeBookOrder, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('shelves/<pk>/change-book-order/', ChangeBookOrder.as_view(),
         name='change_book_order')
]
