from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse

from backend.models import Book
from backend import forms


def Home(request):
    return render(request, 'index.html')

class BookCreate(generic.CreateView):
    model = Book
    form_class = forms.BookForm
    # fields = ['title', 'content', 'image', 'slug', 'user']
    template_name = "book/create.html"
    success_url = reverse_lazy("book-list")
    
class BookList(generic.ListView):
    queryset = Book.objects.filter()
    template_name = "book/list.html"
    context_object_name = "books"
    # paginate_by = 12

class BookDelete(generic.DeleteView):
    model = Book
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy("book-list")
    pk_url_kwarg = "pk"

class BookDetail(generic.DetailView):
    queryset = Book.objects.all()
    template_name = "book/detail.html"
    context_object_name = "book"
    pk_url_kwarg = "pk"

class BookUpdate(generic.UpdateView):
    model = Book
    form_class = forms.BookForm
    template_name = "book/update.html"
    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("book-detail", kwargs={"pk": pk})
    # success_url = reverse_lazy("book-detail")
    pk_url_kwarg = "pk"




