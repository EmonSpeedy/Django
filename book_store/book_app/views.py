from django.shortcuts import render, redirect
from django.db.models.query import QuerySet
from book_app.forms import BookStoreForm
from book_app.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.

# function based view
# def home(request):
#     return render(request, 'home.html')

# class based view
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'Rahim', 'age':21}
        print(context)
        context.update(kwargs)
        print(context)
        return context
        

# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('showbook')
    
#     else:
#         book = BookStoreForm()
#     return render(request, 'store_book.html', {'form' : book})

# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('showbook')
#     def form_valid(self, form):
#         form.save()
#         return redirect('showbook')

# Shortcut method of BookFormView
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')


# function based
# def show_book(request):
#     book = BookStoreModel.objects.all()
#     return render(request, 'show_book.html', {'data' : book})

# class based view
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'booklist'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(id = '3')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'James' : BookStoreModel.objects.all().order_by('author')}
    #     return context
    # ordering = ['-id']
    # def get_template_names(self): # It override the templates
    #     if self.request.user.is_superuser:
    #         template_name = 'superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'staff.html'
    #     else:
    #         template_name = self.template_name
        


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        book = BookStoreForm(request.POST, instance=book)
        if book.is_valid():
            book.save()
            return redirect('showbook')
    return render(request, 'store_book.html', {'form' : form})

class BookUpdateView(UpdateView):
    form_class = BookStoreForm
    model = BookStoreModel
    template_name = 'store_book.html'
    success_url = reverse_lazy('showbook')
    
def delete_book(request, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('showbook')

class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'confirmdelete.html'
    success_url = reverse_lazy('showbook')

class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'bookdetails.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
