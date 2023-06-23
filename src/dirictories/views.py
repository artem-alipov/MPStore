from django.shortcuts import render
from random import randint
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from pathlib import Path

from . import models

#Author
class AuthorsView(generic.ListView):
    model = models.Author
    template_name = "MPShop/author/authors.html"

class DeleteAuthorsView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("staff:login")
    model = models.Author
    template_name = "MPShop/author/delete_authors.html"
    success_url = "/dirictories/success"

class AddAuthorsView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("staff:login")
    model = models.Author
    fields = [
        'author_name', 'author_description'
    ]
    template_name = "MPShop/author/add_authors.html" 
        
class UpdateAuthorsView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("staff:login")
    model = models.Author
    fields = [
        'author_name', 'author_description'
    ]
    template_name = "MPShop/author/update_authors.html"



#Genre
class GenreListView(generic.ListView):
    model = models.Genre
    template_name = 'MPShop/genre/genres.html'

class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("staff:login")
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = 'MPShop/genre/create_genre.html'

class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("staff:login")
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = 'MPShop/genre/update_genre.html'

class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("staff:login")
    model = models.Genre
    template_name = 'MPShop/genre/delete_genre.html'
    success_url = "/dirictories/success"



#Publishion
class PublicationView(generic.ListView):
    model = models.Publication
    template_name = 'MPShop/publication/publication.html'

class PublicationCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("staff:login")
    model = models.Publication
    fields = [
        'publication_name', 'publication_description'
    ]
    template_name = 'MPShop/publication/create_publication.html'

class PublicationUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("staff:login")
    model = models.Publication
    fields = [
        'publication_name', 'publication_description'
    ]
    template_name = 'MPShop/publication/update_publication.html'

class PublicationDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("staff:login")
    model = models.Publication
    template_name = 'MPShop/publication/delete_publication.html'
    success_url = "/dirictories/success"



#Series
class SeriesView(generic.ListView):
    model = models.Series
    template_name = 'MPShop/series/series.html'

class SeriesCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("staff:login")
    model = models.Series
    fields = [
        'series_name', 'series_description'
    ]
    template_name = 'MPShop/series/create_series.html'

class SeriesUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("staff:login")
    model = models.Series
    fields = [
        'series_name', 'series_description'
    ]
    template_name = 'MPShop/series/update_series.html'

class SeriesDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("staff:login")
    model = models.Series
    template_name = 'MPShop/series/delete_series.html'
    success_url = "/dirictories/success"



#Books
class BookView(generic.ListView):
    model = models.Book
    template_name = 'MPShop/book/books.html'

class ViewBook(generic.DetailView):
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'author', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishion', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'MPShop/book/view_book.html'
    
class BookCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("staff:login")
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'author', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishion', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'MPShop/book/create_books.html'

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("staff:login")
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'author', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishion', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'MPShop/book/update_books.html'

    def get_success_url(self) -> str:
        # resizer(self.object.book_image)
        return super().get_success_url()

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("staff:login")
    model = models.Book
    template_name = 'MPShop/book/delete_books.html'
    success_url = "/dirictories/success"

# def resizer(image):
#      extention = image.file.name.split('.')[-1]
#      BASE_DIR = Path(image.file.name).resolve().parent
#      file_name = Path(image.file.name).resolve().name.split('.')
#      for m_basewidth in [250, 40]:
#        im = Image.open(image.file.name)
#        wpercent = (m_basewidth / float(im.size[0]))
#        hsize = int(float(im.size[1]) * float(wpercent))
#        im.thumbnail((m_basewidth, hsize), Image.Resampling.LANCZOS)
#        im.save(str(BASE_DIR / "".join(file_name[:-1])) + f'_{m_basewidth}.' + extention)



def success_page(request):
    return render(
        request,
        template_name='MPShop/success.html'
    )