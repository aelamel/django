from django.urls.conf import path
from blog import views


urlpatterns = [
    path("", views.index,name="articles_index"),
    path("<int:id>", views.show, name="show_article"),
    path("create", views.create, name="create_article"),
    path("edit/<int:id>", views.edit, name="edit_article"),
    path("delete/<int:id>", views.delete, name="delete_article")
]