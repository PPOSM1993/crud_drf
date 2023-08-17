from django.urls import path
from . import views


urlpatterns = [
    #EXAMPLE
    path('', views.index, name=''),
    
    #LIST
    path('category_list', views.CategoryList, name='category_list'),
    path('language_list', views.LanguageList, name='language_list'),
    path('binding_list', views.BindingList, name='binding_list'),
    path('author_list', views.AuthorList, name='author_list'),
    path('format_book_list', views.FormatBookList, name='format_book_list'),
    path('book_list', views.BookList, name='book_list'),
    path('editorial_list', views.EditorialList, name='editorial_list'),
    path('gender_literary_list', views.GenderLiteraryList, name='gender_literary_list'),
    
    #DETAIL
    path('category_detail/<str:pk>/', views.CategoryDetail, name='category_detail'),
    path('language_detail/<str:pk>/', views.LanguageDetail, name='language_detail'),
    path('binding_detail/<str:pk>/', views.BindingDetail, name='binding_detail'),
    path('author_detail/<str:pk>/', views.AuthorDetail, name='author_detail'),
    path('book_detail/<str:pk>/', views.BookDetail, name='book_detail'),
    path('editorial_detail/<str:pk>/', views.EditorialDetail, name='editorial_detail'),
    path('gender_literary/<str:pk>/', views.GenderLiteraryDetail, name='gender_literary'),
    path('format_book_detail/<str:pk>/', views.FormatBookDetail, name='format_book_detail'),
    
    #CREATE
    path('create_category', views.CreateCategory, name='create_category'),
    path('create_language', views.CreateLanguage, name='create_language'),
    path('create_binding', views.CreateBinding, name='create_binding'),
    path('create_author', views.CreateAuthor, name='create_author'),
    path('create_book', views.CreateBook, name='create_book'),
    path('create_editorial', views.CreateEditorial, name='create_editorial'),
    path('create_format_book', views.CreateFormatBook, name='create_format_book'),
    path('create_gender_literary', views.CreateGenderLiterary, name='create_gender_literary'),
    
    #UPDATE
    path('update_category/<str:pk>/', views.UpdateCategory, name='update_category'),
    path('update_language/<str:pk>/', views.UpdateLanguage, name='update_language'),
    path('update_author/<str:pk>/', views.UpdateAuthor, name='update_author'),
    path('update_book/<str:pk>/', views.UpdateBook, name='update_book'),
    path('update_editorial/<str:pk>/', views.UpdateEditorial, name='update_editorial'),
    path('update_format_book/<str:pk>/', views.UpdateFormatBook, name='update_format_book'),
    path('update_binding/<str:pk>/', views.UpdateBinding, name='update_binding'),
    path('update_gender_literary/<str:pk>/', views.UpdateGenderLiterary, name='update_gender_literary'),

    #DELETE
    path('delete_category/<str:pk>/', views.DeleteCategory, name='delete_category'),
    path('delete_language/<str:pk>/', views.DeleteLanguage, name='delete_language'),
    path('delete_binding/<str:pk>/', views.DeleteBinding, name='delete_binding'),
    path('delete_book/<str:pk>/', views.DeleteBook, name='delete_book'),
    path('delete_author/<str:pk>/', views.DeleteAuthor, name='delete_author'),
    path('delete_gender_literary/<str:pk>/', views.DeleteGenderLiterary, name='delete_gender_literary'),
    path('delete_format_book/<str:pk>/', views.DeleteFormatBook, name='delete_format_book'),
    path('delete_editorial/<str:pk>/', views.DeleteEditorial, name='delete_editorial'),
]