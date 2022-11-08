from django.urls import path
from . import views
urlpatterns = [
  #notes/
  path('', views.index_view, name='notes_index'),
  #notes/id
  path('<int:nid>', views.detail_view, name='notes_detail'),
  #notes/new
  path('new', views.create_view, name='notes_new'),
  #notes/edit/id
  path('edit/<int:nid>', views.update_view, name='notes_update'),
  #notes/delete/id
  path('delete/<int:nid>', views.delete_view, name='notes_delete'),
]
