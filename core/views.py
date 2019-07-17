import json

from django.db.models import Prefetch, Q
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

from core.models import Author, Shelf, ShelfBooks


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Shelf.objects.prefetch_related(
        Prefetch(
            'books',
            queryset=ShelfBooks.objects.select_related('book').order_by(
                'order'))
    )


class AuthorListView(ListView):
    template_name = 'authors.html'
    model = Author

    def get_queryset(self):
        query = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            query = query.filter(
                Q(first_name__icontains=q) | Q(last_name__icontains=q)
            )
        return query


class AuthorDetailView(DetailView):
    template_name = 'author.html'
    model = Author


class ChangeBookOrder(View):

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)

        shelf_id = kwargs.get('pk')
        book_id = payload.get('bookId')
        new_index = payload.get('newIndex')

        item = ShelfBooks.objects.get(shelf=shelf_id, book=book_id)
        item.to(new_index)

        return HttpResponse()
