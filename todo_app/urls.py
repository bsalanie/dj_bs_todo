from django.urls import path

from . import views

urlpatterns = [
    path(
        "", views.ListListView.as_view(), name="index"
    ),  # a call to the home page links to the ListListView,
    # which will retrieve all the to-do lists from the database and display them in the 'index.htnl' template
    path(
        "list/<int:list_id>/", views.ItemListView.as_view(), name="list"
    ),  # a call to the list/3 page links to the 3rd ToDoItem; it passes list_id to the view
    # create for ToDoList
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    # delete for ToDoList
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    # create for ToDoItem
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    # update for ToDoItem
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
    # delete for ToDoItem
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),
]
