from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.TemplateView.as_view(template_name = 'home.html')),
    path('<int:roll>/', views.MyTemplateView.as_view(), {'author':'Kila'},name = 'homepage'),
    # path('storebook/', views.store_book, name = 'storebook'),
    path('storebook/', views.BookFormView.as_view(), name = 'storebook'),
    # path('showbook/', views.show_book, name = 'showbook'),
    path('showbook/', views.BookListView.as_view(), name = 'showbook'),
    path('bookdetails/<int:id>', views.BookDetailsView.as_view(), name = 'bookdetails'),
    # path('editbook/<int:id>', views.edit_book, name = 'editbook'),
    path('editbook/<int:pk>', views.BookUpdateView.as_view(), name = 'editbook'),
    # path('deletebook/<int:id>', views.delete_book, name = 'deletebook'),
    path('deletebook/<int:pk>', views.DeleteBookView.as_view(), name = 'deletebook'),
]

