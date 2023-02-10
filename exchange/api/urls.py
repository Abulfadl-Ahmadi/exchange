from django.urls import path
from .views import *

urlpatterns = [
    # path('', Home, name='home'),
    path('books/', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
    path('api/book/', BookApiView.as_view(), name='book-api')
]
