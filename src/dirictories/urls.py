from django.urls import path

from . import views

app_name = 'dirictories'

urlpatterns = [
  #Author
      path('authors/', views.AuthorsView.as_view(), name="authors-view"),
      path('add_authors/', views.AddAuthorsView.as_view(), name="add-authors"),
      path('delete_authors/<int:pk>', views.DeleteAuthorsView.as_view(), name="delete-authors"),
      path('update_authors/<int:pk>', views.UpdateAuthorsView.as_view(), name="update-authors"),
  #Genre
      path('genres/', views.GenreListView.as_view(), name="genre-list-view"),
      path('create_genre/', views.GenreCreateView.as_view(), name="create-genre"),
      path('delete_genre/<int:pk>', views.GenreDeleteView.as_view(), name="delete-genre"),
      path('update_genre/<int:pk>', views.GenreUpdateView.as_view(), name="update-genre"),
  #Publication
      path('publishion/', views.PublicationView.as_view(), name="Publication-view"),
      path('create_publishion/', views.PublicationCreateView.as_view(), name="create-Publication"),
      path('delete_publishion/<int:pk>', views.PublicationDeleteView.as_view(), name="delete-Publication"),
      path('update_publishion/<int:pk>', views.PublicationUpdateView.as_view(), name="update-Publication"),
  #Series
      path('series/', views.SeriesView.as_view(), name="series-view"),
      path('create_series/', views.SeriesCreateView.as_view(), name="create-series"),
      path('delete_series/<int:pk>', views.SeriesDeleteView.as_view(), name="delete-series"),
      path('update_series/<int:pk>', views.SeriesUpdateView.as_view(), name="update-series"),
  #Books
      path('books/', views.BookView.as_view(), name="book-view"),
      path('view_book/<int:pk>', views.ViewBook.as_view(), name="view-book"),
      path('create_books/', views.BookCreateView.as_view(), name="create-book"),
      path('delete_books/<int:pk>', views.BookDeleteView.as_view(), name="delete-book"),
      path('update_books/<int:pk>', views.BookUpdateView.as_view(), name="update-book"),

      path('success/', views.success_page, name="success-page")
]